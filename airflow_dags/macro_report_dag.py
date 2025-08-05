
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.collector import coletar_todos

def macro_pipeline():
    resultados = coletar_todos()
    for ind, status in resultados.items():
        print(f"{ind.upper()}: {status}")

with DAG('macro_report_pipeline',
         start_date=datetime(2023, 1, 1),
         schedule_interval='@weekly',
         catchup=False) as dag:

    t1 = PythonOperator(
        task_id='run_macro_agents',
        python_callable=macro_pipeline
    )
    t1
