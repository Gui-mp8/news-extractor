import os

from utils.config import load_config
from datasources.the_guardian import TheGuardian
from analytics.bigquery import BigQueryR

def main(config):

    bq = BigQueryR(
            project_name=config["project_id"],
        )

    bq.create_dataset()
    bq.create_table()

    the_guardian = TheGuardian()

    for site_url in config["extraction"]["site"]["the_guardian"]["urls"]:

        the_guardian.site_url = site_url
        data = the_guardian.get_structured_page_content()
        bq.insert_rows(data=data)



if __name__ == '__main__':
    config = load_config()
    main(config)