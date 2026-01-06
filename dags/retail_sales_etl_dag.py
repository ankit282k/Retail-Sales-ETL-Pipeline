from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="retail_sales_etl",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "retail"]
) as dag:

    start = EmptyOperator(task_id="start")

    extract = EmptyOperator(task_id="extract")

    transform = EmptyOperator(task_id="transform")

    load = EmptyOperator(task_id="load")

    end = EmptyOperator(task_id="end")

    start >> extract >> transform >> load >> end