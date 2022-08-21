CREATE DATABASE StationeryItems;
USE StationeryItems;
CREATE TABLE item_list(id INT NOT NULL AUTO_INCREMENT, item_name VARCHAR(255) NOT NULL, item_price FLOAT NOT NULL, PRIMARY KEY(id));
CREATE TABLE selected_items(id INT NOT NULL AUTO_INCREMENT, item_id INT NOT NULL, qty FLOAT NOT NULL, price FLOAT NOT NULL, PRIMARY KEY(id));
ALTER TABLE selected_items ADD selected_item_name VARCHAR(255) NOT NULL AFTER item_id;
CREATE TABLE logs(id INT NOT NULL AUTO_INCREMENT, selected_item_id INT NOT NULL, selected_qty FLOAT NOT NULL,price FLOAT,date_time DATETIME, PRIMARY KEY(id));
