DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR (255),
    country VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    prod_name VARCHAR(255),
    prod_desc VARCHAR(255),
    stock_qty INT,
    buy_cost FLOAT,
    sell_price FLOAT,
    imported BOOLEAN,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    qty INT,
    product_id INT REFERENCES products(id) ON DELETE CASCADE
);