# assemblyline-service-template

A template repository for Assemblyline 4 services.

## Usage

Install jq via `sudo apt install jq`

Install / Update `cookiecutter` and `cruft`:

```bash
pip install -Ur requirements.txt
```

Go to your development work directory where you want to create your service and run:

```bash
cruft create git@github.com:CybercentreCanada/assemblyline-service-template.git
# or
cruft create https://github.com/CybercentreCanada/assemblyline-service-template.git
```

## Input variables

You will be asked to fill in some variables.

|   **Parameter**   | **Description**                                                                                                                       |
| :---------------: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   service_name    | The name of the service you are creating                                                                                              |
| short_description | A short one or two line description of what this service does                                                                         |
|       stage       | The Assembyline stage that this service should run at                                                                                 |
|     category      | The type of service you are creating                                                                                                  |
|   org_name_full   | The full name of your organization, as you would like displayed in the License                                                        |
|  org_name_short   | An abbreveation of the organization name (used in the docker repoistory path)                                                         |
|      license      | The license you would like to use for this service. If `none` is selected, an empty LICENSE file will be created for you to fill out. |

## Writing the service

Once the project has been generated, you will need to manually:

- Write the service;
- Add any heuristics to the `service_manifest.yml` if applicable;

## Keeping the service in-sync with the template

To check if the service doesn't have the latest template changes, run:

```bash
cruft check
```

To update, simply run:

```bash
cruft update
```

You will then need to review any changes before they are applied.
