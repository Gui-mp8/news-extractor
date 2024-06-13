from typing import List, Dict, Any
from google.cloud import bigquery

from interfaces.repository import IRepository

class BigQueryR(IRepository):
    def __init__(self, project_name: str, dataset_name: str, table_name: str) -> None:
        self.client = bigquery.Client(project=project_name)
        self.dataset_name = dataset_name
        self.table_name = table_name

    def create_dataset(self) -> None:
        dataset_ref = self.client.dataset(self.dataset_name)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"

        try:
            self.client.get_dataset(dataset_ref)
            print(f"Dataset {self.dataset_name} already exists.")
        except Exception:
            dataset = self.client.create_dataset(dataset)
            print(f"Dataset {self.dataset_name} created.")

    def create_table(self) -> None:
        table_ref = self.client.dataset(self.dataset_name).table(self.table_name)

        schema = [
            bigquery.SchemaField("article_date", "STRING"),
            bigquery.SchemaField("title", "STRING"),
            bigquery.SchemaField("subtitle", "STRING"),
            bigquery.SchemaField("content", "STRING"),
            bigquery.SchemaField("article", "STRING"),
            bigquery.SchemaField("author", "STRING"),
            bigquery.SchemaField("author_profile_link", "STRING"),
        ]

        table = bigquery.Table(table_ref, schema=schema)

        try:
            self.client.get_table(table_ref)
            print(f"Table {self.table_name} already exists.")
        except Exception:
            table = self.client.create_table(table)
            print(f"Table {self.table_name} created.")

    def check_existing_rows(self, urls: List[str]) -> List[str]:
        query = f"""
        SELECT article
        FROM `{self.client.project}.{self.dataset_name}.{self.table_name}`
        WHERE article IN UNNEST(@urls)
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("urls", "STRING", urls)
            ]
        )

        query_job = self.client.query(query, job_config=job_config)
        result = query_job.result()

        existing_urls = [row.article for row in result]
        return existing_urls

    def insert_rows(self, data: List[Dict[str, Any]]) -> None:
        table_ref = self.client.dataset(self.dataset_name).table(self.table_name)

        urls = [item['article'] for item in data]
        existing_urls = self.check_existing_rows(urls)

        new_data = [item for item in data if item['article'] not in existing_urls]

        if new_data:
            job_config = bigquery.LoadJobConfig(
                write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
                schema=[
                    bigquery.SchemaField("article_date", "STRING"),
                    bigquery.SchemaField("title", "STRING"),
                    bigquery.SchemaField("subtitle", "STRING"),
                    bigquery.SchemaField("content", "STRING"),
                    bigquery.SchemaField("article", "STRING"),
                    bigquery.SchemaField("author", "STRING"),
                    bigquery.SchemaField("author_profile_link", "STRING"),
                ],
            )

            load_job = self.client.load_table_from_json(
                new_data,
                table_ref,
                job_config=job_config
            )

            load_job.result()  # Wait for the job to complete.

            print(f"New rows have been added: {len(new_data)} rows.")
        else:
            print("No new rows to add.")