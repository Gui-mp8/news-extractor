import os

from datasources.the_guardian import TheGuardian
from analytics.bigquery import BigQueryR

def main():
    the_guardian = TheGuardian()
    the_guardian.site_url = "https://www.theguardian.com/au"
    data = the_guardian.get_structured_page_content()

    bq = BigQueryR(
            project_name="news-extraction-426201",
            dataset_name="challenge",
            table_name="news"
        )

    bq.create_dataset()
    bq.create_table()
    bq.insert_rows(data=data)



if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./news-extraction.json"
    main()