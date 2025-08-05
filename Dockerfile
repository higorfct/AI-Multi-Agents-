FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV AIRFLOW_HOME=/app/airflow
RUN mkdir -p $AIRFLOW_HOME

CMD ["airflow", "standalone"]
