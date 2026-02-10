CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id BIGINT PRIMARY KEY,
    country TEXT
);

CREATE TABLE IF NOT EXISTS dim_products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    price NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS dim_stores (
    store_id TEXT PRIMARY KEY,
    store_name TEXT,
    region TEXT,
    country TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

CREATE TABLE IF NOT EXISTS fact_sales (
    order_id TEXT,
    order_date DATE,
    description TEXT,
    product_id TEXT,
    store_id TEXT,
    quantity INT,
    country TEXT,
    price NUMERIC(10,2),
    revenue NUMERIC(12,2),
    PRIMARY KEY (order_id, product_id)
);

CREATE TABLE IF NOT EXISTS stg_customers (
    customer_id BIGINT,
    country TEXT
);

CREATE TABLE IF NOT EXISTS stg_products (
    product_id TEXT,
    product_name TEXT,
    price NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS stg_stores (
    store_id TEXT,
    store_name TEXT,
    region TEXT,
    country TEXT
);
