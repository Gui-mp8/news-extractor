# News Extractor

This project scraps data from [the guardian](https://www.theguardian.com/au), ingest the data in a `BigQuery table` and then raise an `API` that consume the data from BigQuery. Moreover, a Design Pattern called [Repository](https://python.plainenglish.io/design-patterns-in-python-repository-pattern-1c2e5070a01c) was used to make a well structured code.

## Pre-Requisites
Before running the code, you must have this tools installed:

- [Python](https://www.python.org/downloads/)

- [Docker](https://docs.docker.com/engine/install/ubuntu/)

- [docker compose plugin](https://docs.docker.com/compose/install/linux/#install-using-the-repository) updated

- [Google Cloud Account](https://cloud.google.com/free?hl=en)

## Configuration

After creating the Google Cloud Account you will need pass trough some steps

- Step 1 : [Create a Service Account and Add Owner permission](https://www.youtube.com/watch?v=aD9vU1a7WXo) to easily run the code

- Step 2 : [Create a service account key](https://youtu.be/dj9fxiuz4WM?t=66)

- Step 3 : save it with the name of `news-extraction.json`, or change the key name on Dockerfiles

## Execution

You must create **two** shell enviroments


- At the first one you will run:

```
docker compose up
```
- At the second one you will consume the API with this command

```
curl -i http://0.0.0.0:8000/content/pandas
```

Note that i write pandas after content, that means that i'm searching for content that has pandas on it.