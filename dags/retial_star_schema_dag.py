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

    load_customers = PythonOperator(
        task_id="load_dim_customers",
        python_callable=load_dimension,
        op_args=["/usr/local/airflow/data/customers.csv", "dim_customers"]
    )

    load_products = PythonOperator(
        task_id="load_dim_products",
        python_callable=load_dimension,
        op_args=["/usr/local/airflow/data/products.csv", "dim_products"]
    )

    load_stores = PythonOperator(
        task_id="load_dim_stores",
        python_callable=load_dimension,
        op_args=["/usr/local/airflow/data/stores.csv", "dim_stores"]
    )

    load_fact_sales = PythonOperator(
        task_id="load_fact_sales",
        python_callable=load_fact,
        op_args=["/usr/local/airflow/data/sales.csv"]
    )

    create_tables >> [load_customers, load_products, load_stores] >> load_fact_sales
