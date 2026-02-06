import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@retail-sales-etl-pipeline_58ac6a-postgres-1:5432/retail_db"
)

def load_fact(csv_path):
    df = pd.read_csv(csv_path)
    df["revenue"] = df["quantity"] * df["price"]
    df.to_sql("fact_sales", engine, if_exists="replace", index=False)
