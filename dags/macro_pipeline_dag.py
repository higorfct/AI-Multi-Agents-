from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append('/opt/airflow/langgraph_agents')
sys.path.append('/opt/airflow')

from pib_agent import agent as pib_agent
from inflacao_agent import agent as inflacao_agent
from cambio_agent import agent as cambio_agent
from juros_agent import agent as juros_agent
from send_email import send_email

def run_agent(agent, nome):
    result = agent.invoke({})
    relatorio = result['analysis']
    path = f"/opt/airflow/reports/{nome}_{datetime.now().date()}.txt"
    with open(path, "w") as f:
        f.write(relatorio)
    send_email(f"[Relatório] {nome.upper()}", relatorio)

default_args = {
    'owner': 'airflow',
    'retry_delay': timedelta(minutes=10),
    'retries': 1
}

with DAG('macro_pipeline_dag',
         start_date=datetime(2025, 8, 1),
         schedule_interval=None,
         default_args=default_args,
         catchup=False) as dag:

    t1 = PythonOperator(task_id='analise_pib', python_callable=lambda: run_agent(pib_agent, "pib"))
    t2 = PythonOperator(task_id='analise_inflacao', python_callable=lambda: run_agent(inflacao_agent, "inflacao"))
    t3 = PythonOperator(task_id='analise_cambio', python_callable=lambda: run_agent(cambio_agent, "cambio"))
    t4 = PythonOperator(task_id='analise_juros', python_callable=lambda: run_agent(juros_agent, "juros"))
