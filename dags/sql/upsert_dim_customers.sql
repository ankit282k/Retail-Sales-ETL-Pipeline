INSERT INTO dim_customers (customer_id, country)
SELECT DISTINCT customer_id, country
FROM stg_customers
ON CONFLICT (customer_id)
DO UPDATE SET
    country = EXCLUDED.country;
