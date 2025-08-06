FROM python:3.10

ENV AIRFLOW_HOME=/opt/airflow

RUN pip install apache-airflow==2.9.1 \
    langgraph \
    llama-cpp-python \
    pandas \
    matplotlib \
    requests \
    python-dotenv

COPY . $AIRFLOW_HOME
WORKDIR $AIRFLOW_HOME
