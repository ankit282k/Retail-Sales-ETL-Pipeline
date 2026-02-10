INSERT INTO dim_products (product_id, product_name, price)
SELECT DISTINCT product_id, product_name, price
FROM stg_products
ON CONFLICT (product_id)
DO UPDATE SET
    product_name = EXCLUDED.product_name,
    price = EXCLUDED.price;
