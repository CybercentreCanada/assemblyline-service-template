# Assemblyline Service Template

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

|    **Parameter**     | **Description**                                                                                                                       |
| :------------------: | ------------------------------------------------------------------------------------------------------------------------------------- |
|     service_name     | The name of the service you are creating                                                                                              |
|  short_description   | A short one or two line description of what this service does                                                                         |
| short_description_fr | In French, a short one or two line description of what this service does                                                              |
|        stage         | The Assembyline stage that this service should run at                                                                                 |
|       category       | The type of service you are creating                                                                                                  |
|    org_name_full     | The full name of your organization, as you would like displayed in the License                                                        |
|    org_name_short    | An abbreveation of the organization name (used in the docker repoistory path)                                                         |
|       license        | The license you would like to use for this service. If `none` is selected, an empty LICENSE file will be created for you to fill out. |

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

---

# Modèle de service pour Assemblyline 4

Un référentiel de modèles pour les services Assemblyline 4.

## Utilisation

Installer jq via `sudo apt install jq`

Installer / mettre à jour `cookiecutter` et `cruft` :

``bash
pip install -Ur requirements.txt

```

Allez dans votre répertoire de développement où vous voulez créer votre service et exécutez :

``bash
cruft create git@github.com:CybercentreCanada/assemblyline-service-template.git
# ou
cruft create https://github.com/CybercentreCanada/assemblyline-service-template.git
```

## Variables d'entrée

Il vous sera demandé de remplir quelques variables.

|    **Paramètre**     | **Description**                                                                                                                                         |
| :------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     service_name     | Le nom du service que vous créez.                                                                                                                       |
|  short_description   | Une courte description d'une ou deux lignes de ce que fait ce service.                                                                                  |
| short_description_fr | En français, une brève description d'une ou deux lignes de ce que fait ce service                                                                       |
|        stage         | L'étape d'Assembyline à laquelle ce service doit s'exécuter                                                                                             |
|       category       | Le type de service que vous créez                                                                                                                       |
|    org_name_full     | Le nom complet de votre organisation, tel que vous souhaitez qu'il soit affiché dans la licence.                                                        |
|    org_name_short    | Une abbréviation du nom de votre organisation (utilisé pour le nom des images docker).                                                                  |
|       licence        | La licence que vous souhaitez utiliser pour ce service. Si `none` est sélectionné, un fichier LICENSE vide sera créé pour que vous puissiez le remplir. |

## Écrire le service

Une fois le projet généré, vous devrez manuellement :

- Écrire le service ;
- Ajouter les heuristiques au fichier `service_manifest.yml`, si applicable ;

## Maintenir le service en synchronisation avec le modèle

Pour vérifier si le service n'a pas les dernières modifications du modèle, exécutez :

```bash
cruft check
```

Pour mettre à jour, exécutez simplement:

```bash
cruft update
```

Vous devrez ensuite vérifier les changements avant qu'ils ne soient appliqués.
