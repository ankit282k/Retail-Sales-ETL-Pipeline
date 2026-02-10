from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator as PostgresOperator
from datetime import datetime
from include.load_dimensions import load_dimension
from include.load_fact import load_fact

with DAG(
    dag_id="retail_star_schema_etl",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    create_tables = PostgresOperator(
        task_id="create_tables",
        conn_id="postgres_default",
        sql="sql/create_tables.sql"
    )

    create_tables