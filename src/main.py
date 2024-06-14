import os

from utils.config import load_config
from datasources.the_guardian import TheGuardian
from analytics.bigquery import BigQueryR

def main(config):
    
    print(config)
    
    the_guardian = TheGuardian()
    
    for table in config["extraction"]["site"]["the_guardian"]["table"]:
        
        the_guardian.site_url = table["site_url"]
        data = the_guardian.get_structured_page_content()

        bq = BigQueryR(
                project_name=config["project_id"],
                dataset_name=config["extraction"]["site"]["the_guardian"]["dataset_name"],
                table_name=table["name"]
            )

        bq.create_dataset()
        bq.create_table()
        bq.insert_rows(data=data)



if __name__ == '__main__':
    config = load_config()
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./news-extraction.json"
    main(config)