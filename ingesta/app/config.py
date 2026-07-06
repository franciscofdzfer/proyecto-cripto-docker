import os

DB_HOST = os.environ.get("POSTGRES_HOST", "postgres")
DB_NAME = os.environ.get("POSTGRES_DB", "cripto_db")
DB_USER = os.environ.get("POSTGRES_USER", "francisco")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "clase123")

MONEDAS = ["bitcoin", "ethereum", "solana"]
API_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(MONEDAS)}&vs_currencies=usd"
