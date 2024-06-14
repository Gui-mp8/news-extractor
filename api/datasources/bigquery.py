from typing import List, Dict, Any
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
from api.interfaces.repository import IRepository
from api.utils.config import load_config

class BigQueryR(IRepository):
    def __init__(self) -> None:
        self.config = load_config()
        self.client = bigquery.Client(project=self.config["project_id"])
        self.dataset_name = "the_guardian"
        self.table_name = "daily_jornal_data"
        self.table_id = f"{self.config['project_id']}.{self.dataset_name}.{self.table_name}"

    def all_data(self) -> List[Dict[str, Any]]:
        query = f"""
            SELECT * FROM `{self.table_id}`
        """
        try:
            query_job = self.client.query(query)
            results = query_job.result()
            rows = [dict(row) for row in results]
            return rows
        except GoogleAPIError as e:
            print(f"An error occurred: {e}")
            return []

    def filter_by_keyword(self, keyword: str) -> List[Dict[str, Any]]:
        query = f"""
            SELECT * FROM `{self.table_id}`
            WHERE LOWER(content) LIKE "%{keyword}%"
        """
        try:
            query_job = self.client.query(query)
            results = query_job.result()
            rows = [dict(row) for row in results]
            return rows
        except GoogleAPIError as e:
            print(f"An error occurred: {e}")
            return []
