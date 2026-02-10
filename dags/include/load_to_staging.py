import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
)

def load_to_staging(csv_path, staging_table):
    df = pd.read_csv(csv_path)
    df.to_sql(staging_table, engine, if_exists="append", index=False)
