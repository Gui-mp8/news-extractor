from typing import List, Dict, Any
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
from api.interfaces.repository import IRepository

class BigQueryR(IRepository):
    def __init__(self) -> None:
        self.client = bigquery.Client(project="news-extraction-426201")
        self.dataset_name = "challenge"
        self.table_name = "news"
        self.table_id = f"news-extraction-426201.{self.dataset_name}.{self.table_name}"

    def get_by_word_in_content(self) -> List[Dict[str, Any]]:
        query = f"""
            SELECT * FROM `{self.table_id}`
        """
    # def get_by_word_in_content(self, word: str) -> List[Dict[str, Any]]:
    #     query = f"""
    #         SELECT * FROM `{self.table_id}`
    #         WHERE LOWER(content) LIKE "%{word}%"
    #     """
        try:
            query_job = self.client.query(query)
            results = query_job.result()  # Waits for job to complete.
            rows = [dict(row) for row in results]
            return rows
        except GoogleAPIError as e:
            print(f"An error occurred: {e}")
            return []
