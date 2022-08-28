CREATE DATABASE billing_app;
USE billing_app;
CREATE TABLE item_list(id INT NOT NULL AUTO_INCREMENT, item_name VARCHAR(255) NOT NULL, item_price FLOAT NOT NULL, PRIMARY KEY(id));
CREATE TABLE selected_items(id INT NOT NULL AUTO_INCREMENT, item_id INT NOT NULL, qty FLOAT NOT NULL, price FLOAT NOT NULL, PRIMARY KEY(id));
ALTER TABLE selected_items ADD selected_item_name VARCHAR(255) NOT NULL AFTER item_id;
CREATE TABLE logs(id INT NOT NULL AUTO_INCREMENT, selected_item_id INT NOT NULL, selected_qty FLOAT NOT NULL,price FLOAT,date_time DATETIME, PRIMARY KEY(id));
INSERT INTO item_list(item_name,item_price) VALUES('item1',100);
INSERT INTO item_list(item_name,item_price) VALUES('item2',20);
INSERT INTO item_list(item_name,item_price) VALUES('item3',200);
INSERT INTO item_list(item_name,item_price) VALUES('item4',184);
INSERT INTO item_list(item_name, item_price ) VALUES('test1',10);
