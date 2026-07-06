from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "francisco",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="pipeline_cripto",
    description="Carga continuada de precios cripto + transformaciones DBT (staging -> test -> marts)",
    default_args=default_args,
    schedule_interval="*/5 * * * *",
    start_date=datetime(2026, 7, 6),
    catchup=False,
    tags=["cripto", "dbt"],
) as dag:

    carga_continuada = BashOperator(
        task_id="carga_continuada",
        bash_command=(
            "cd /opt/proyecto_cripto && "
            "docker compose run --rm ingesta app.carga_continuada"
        ),
    )

    dbt_staging = BashOperator(
        task_id="dbt_staging",
        bash_command=(
            "cd /opt/proyecto_cripto && "
            "docker compose run --rm dbt run --select staging"
        ),
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=(
            "cd /opt/proyecto_cripto && "
            "docker compose run --rm dbt test"
        ),
    )

    dbt_marts = BashOperator(
        task_id="dbt_marts",
        bash_command=(
            "cd /opt/proyecto_cripto && "
            "docker compose run --rm dbt run --select marts"
        ),
    )

    carga_continuada >> dbt_staging >> dbt_test >> dbt_marts
