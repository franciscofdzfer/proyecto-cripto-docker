with fuente as (

    select *
    from {{ source('raw', 'precios_cripto') }}

),

renombrado as (

    select
        id,
        moneda as symbol,
        round(precio_usd, 2) as price_usd,
        fecha as event_time
    from fuente
    where precio_usd is not null
      and precio_usd > 0

)

select * from renombrado
