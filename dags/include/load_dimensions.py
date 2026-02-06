import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@retail-sales-etl-pipeline_58ac6a-postgres-1:5432/retail_db"
)

def load_dimension(csv_path, table_name):
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)


# postgresql://airflow_user:your_secure_password@retail-sales-etl-pipeline_58ac6a-postgres-1:5432/retail_db