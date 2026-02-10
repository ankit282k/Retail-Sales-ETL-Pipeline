INSERT INTO dim_stores (store_id, store_name, region, country)
SELECT DISTINCT store_id, store_name, region, country
FROM stg_stores
ON CONFLICT (store_id)
DO UPDATE SET
    store_name = EXCLUDED.store_name,
    region = EXCLUDED.region,
    country = EXCLUDED.country;
