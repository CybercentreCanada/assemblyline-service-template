import json
import os
import re
import subprocess

import jinja2
from jinja2.ext import Extension

# NOTE: This module deliberately does not reuse the old name
# (local_extensions/github_maintainer.py). During `cruft update`, the extension is
# first imported from the template commit the project is currently pinned to, and
# Python's module cache would then reuse that old code when rendering the new
# template commit. Giving the module a new name guarantees the code below runs as
# soon as a project updates onto a template commit containing it.

# The working directory when this module is imported: for `cruft update` this is
# the root of the project being updated. It cannot be read at render time because
# cookiecutter chdirs into a temporary directory while rendering files.
_PROJECT_DIR = os.getcwd()


@jinja2.pass_context
def github_maintainer(context):
    if "_github_maintainer" in context.parent["cookiecutter"]:
        return True

    # Cruft regenerates the cookiecutter context on every update without private
    # variables, so recover the maintainer recorded in the project being updated
    # before anything else.
    try:
        with open(os.path.join(_PROJECT_DIR, ".cruft.json")) as cruft_file:
            old_cookiecutter = json.load(cruft_file)["context"]["cookiecutter"]
    except (OSError, ValueError, KeyError):
        old_cookiecutter = {}
    github_username = old_cookiecutter.get("_github_maintainer") or ""

    # Projects whose .cruft.json already lost the maintainer in a previously
    # merged update PR still have it in their CODEOWNERS file.
    if not github_username:
        try:
            with open(os.path.join(_PROJECT_DIR, ".github", "CODEOWNERS")) as codeowners_file:
                match = re.search(r"^\*\s+@(\S+)", codeowners_file.read(), re.MULTILINE)
                if match:
                    github_username = match.group(1)
        except OSError:
            pass

    try:
        git_username = subprocess.check_output(
            ["git", "config", "--get", "user.name"],
            text=True,
        ).strip()
    except subprocess.CalledProcessError:
        git_username = ""

    # Fall back to the git username for the initial `cruft create`.
    if not github_username:
        github_username = git_username

    if not github_username:
        raise Exception("Cannot determine your Git username for the CODEOWNERS file.")

    if github_username == "CruftBot":
        # Automated update of a project that has no recorded maintainer: keep the
        # CODEOWNERS file empty rather than assigning it to the bot.
        return False

    context.parent["cookiecutter"]["_github_maintainer"] = github_username

    if git_username == "CruftBot" and "local_extensions.maintainer.Ext" not in old_cookiecutter.get("_extensions", []):
        # Automated update of a project still pinned to a template commit that
        # predates this module: the "current template" side of cruft's diff is
        # rendered by the old extension, which omits the maintainer line for
        # CruftBot. Omit it on this side too so the diff leaves the project's
        # CODEOWNERS (and no *.rej files) alone; the maintainer recovered above
        # is still recorded in .cruft.json for the following updates.
        return False

    return True


class Ext(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        environment.globals["github_maintainer"] = github_maintainer
