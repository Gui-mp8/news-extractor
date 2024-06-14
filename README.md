# News Extractor

This project scraps data from [the guardian](https://www.theguardian.com/au), ingest the data in a `BigQuery table` and then provides an `API` that consume the data from BigQuery.

This project utilizes a Design Pattern called [Repository](https://python.plainenglish.io/design-patterns-in-python-repository-pattern-1c2e5070a01c), which separates the data access logic from the business logic. This makes the codebase more modular, testable, and maintainable.

## Pre-Requisites
Before running the code, ensure you have the following tools installed:

- [Docker](https://docs.docker.com/engine/install/ubuntu/)

- [docker compose plugin](https://docs.docker.com/compose/install/linux/#install-using-the-repository) updated

- [Google Cloud Account](https://cloud.google.com/free?hl=en)

## Configuration

After creating the Google Cloud Account you will need pass trough some steps

- Step 1 : [Create a Service Account and Add BigQuery Admin permission](https://www.youtube.com/watch?v=aD9vU1a7WXo) to easily run the code

- Step 2 : [Create a service account key](https://youtu.be/dj9fxiuz4WM?t=66)

- Step 3 : save it with the name of `news-extraction.json`, or change the key name on both of Dockerfiles

- Step 4 : Modify the file `config.yaml` with the respective data of your project

**OBS** If you want to extract data from other the guardian site topic, follow the examples inside the config.yaml file.

## Execution

Step 1 -  Clone the repository:
```
git clone git@github.com:Gui-mp8/news-extractor.git
```

Step 2 - Create **two** shell enviroments


In the first environment, run:

```
docker compose up
```
In the second environment, consume the API with the following command:

```
curl -i http://0.0.0.0:8000/content/keyword=russia
```

Or you can make a test with any language:
```
# Python Example:

import requests

response = requests.get("http://0.0.0.0:8000/content/keyword=russia")

if response.status_code == 200:

    print("response.json()")

```


`OBS`: Note that i write pandas after content, that means that i'm searching for content that has russia on it.

## Conclusion

The Repository pattern is applied both for data ingestion and extraction, treating any data source as a repository, which enhances modularization and maintenance.
