from app.db import conectar
from app.api_cripto import obtener_precios

def main():
    conn = conectar()
    cur = conn.cursor()

    datos = obtener_precios()
    for moneda, valores in datos.items():
        cur.execute(
            "INSERT INTO RAW.precios_cripto (moneda, precio_usd) VALUES (%s, %s);",
            (moneda, valores["usd"])
        )
    conn.commit()
    print(f"Primera carga insertada: {datos}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
