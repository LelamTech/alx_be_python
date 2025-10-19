-- Create the database
CREATE DATABASE IF NOT EXISTS alx_book_store;

-- Create Authors table
CREATE TABLE IF NOT EXISTS alx_book_store.authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);

-- Create Books table
CREATE TABLE IF NOT EXISTS alx_book_store.books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES alx_book_store.authors(author_id)
);

-- Create Customers table
CREATE TABLE IF NOT EXISTS alx_book_store.customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

-- Create Orders table
CREATE TABLE IF NOT EXISTS alx_book_store.orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES alx_book_store.customers(customer_id)
);

-- Create Order_Details table
CREATE TABLE IF NOT EXISTS alx_book_store.order_details (
    orderdetailid INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES alx_book_store.orders(order_id),
    FOREIGN KEY (book_id) REFERENCES alx_book_store.books(book_id)
);
