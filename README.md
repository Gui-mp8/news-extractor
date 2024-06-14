# News Extractor

This project scraps data from [the guardian](https://www.theguardian.com/au), ingest the data in a `BigQuery table` and then provides an `API` that consume the data from BigQuery.

This project utilizes a Design Pattern called [Repository](https://python.plainenglish.io/design-patterns-in-python-repository-pattern-1c2e5070a01c), which is a well-established pattern that separates the data access logic from the business logic. By using this pattern, the codebase becomes more modular, testable, and maintainable.

## Pre-Requisites
Before running the code, ensure you have the following tools installed:

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

Create **two** shell enviroments


 - In the first environment, run:

```
docker compose up
```
- In the second environment, consume the API with the following command:


```
curl -i http://0.0.0.0:8000/content/word=pandas
```

Note that i write pandas after content, that means that i'm searching for content that has pandas on it.