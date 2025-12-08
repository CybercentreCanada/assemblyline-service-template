import subprocess

import jinja2
from jinja2.ext import Extension


@jinja2.pass_context
def github_maintainer(context):
    if "_github_maintainer" in context.parent["cookiecutter"]:
        return True

    github_username = ""
    try:
        github_username = subprocess.check_output(
            ["git", "config", "--get", "user.name"],
            text=True,
        ).strip()
    except subprocess.CalledProcessError:
        pass

    if not github_username:
        raise Exception("Cannot determine your Git username for the CODEOWNERS file.")

    if github_username == "CruftBot":
        return False

    context.parent["cookiecutter"]["_github_maintainer"] = github_username
    return True


class Ext(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        environment.globals["github_maintainer"] = github_maintainer
