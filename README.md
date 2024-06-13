# News Extractor

This project scraps data from [the guardian](https://www.theguardian.com/au), ingest the data in a `BigQuery table` and then raise an `API` to be consumed.

## Pre-Requisite
Before running the code, you must have has this tools installed:

- [Python](https://www.python.org/downloads/)

- [Docker](https://docs.docker.com/engine/install/ubuntu/)

- [docker compose plugin](https://docs.docker.com/compose/install/linux/#install-using-the-repository) updated

- [Google Cloud Account](https://cloud.google.com/free?hl=en)

## Configuration


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