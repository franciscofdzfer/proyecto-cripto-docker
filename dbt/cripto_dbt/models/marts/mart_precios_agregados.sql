SELECT
    symbol,
    ROUND(AVG(price_usd), 2) AS avg_price_usd,
    MAX(price_usd) AS max_price_usd,
    MIN(price_usd) AS min_price_usd,
    COUNT(*) AS num_registros
FROM {{ ref('stg_precios_cripto') }}
GROUP BY symbol
