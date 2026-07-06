FROM python:3.12-slim

WORKDIR /usr/app

ENV PYTHONUNBUFFERED=1 \
    DBT_PROFILES_DIR=/usr/app/profiles

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --retries 10 --timeout 120 -r requirements.txt

COPY profiles.yml /usr/app/profiles/profiles.yml
COPY cripto_dbt/ /usr/app/cripto_dbt/

WORKDIR /usr/app/cripto_dbt

EXPOSE 8080

# Comando por defecto: servir la documentacion (UI persistente).
# Los jobs (dbt run, dbt build, dbt test...) se lanzan bajo demanda:
#   docker compose run --rm dbt run
#   docker compose run --rm dbt build
# (esto es exactamente lo que hara Airflow contra la imagen 'proyecto-cripto-dbt')
ENTRYPOINT ["dbt"]
CMD ["docs", "serve", "--host", "0.0.0.0", "--port", "8080"]
