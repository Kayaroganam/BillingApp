#Import required modules
import os
import mysql.connector
from mysql.connector import errorcode
import datetime
from variables import var

#try to connect mysql database
try:
    mydb = mysql.connector.connect(
        user=var.Mysql_User, password=var.Mysql_Password, host=var.Mysql_Host, database=var.Mysql_Database
    )
    print("Database connected.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access Denied!")
    
    #if database is not avilable
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Datase doesn't exist!")
        
        mydb = mysql.connector.connect(
        user=var.Mysql_User, password=var.Mysql_Password, host=var.Mysql_Host
        )
        
        my_cursor = mydb.cursor()
        query = f"""
        CREATE DATABASE {var.Mysql_Database};
        USE {var.Mysql_Database};
        CREATE TABLE item_list(id INT NOT NULL AUTO_INCREMENT, item_name VARCHAR(255) NOT NULL, item_price FLOAT NOT NULL, PRIMARY KEY(id));
        CREATE TABLE selected_items(id INT NOT NULL AUTO_INCREMENT, item_id INT NOT NULL, qty FLOAT NOT NULL, price FLOAT NOT NULL, PRIMARY KEY(id));
        ALTER TABLE selected_items ADD selected_item_name VARCHAR(255) NOT NULL AFTER item_id;
        CREATE TABLE logs(id INT NOT NULL AUTO_INCREMENT, selected_item_id INT NOT NULL, selected_qty FLOAT NOT NULL,price FLOAT,date_time DATETIME, PRIMARY KEY(id));
        """
        
        my_cursor.execute(query)
        print("database created.")

        mydb = mysql.connector.connect(
        user=var.Mysql_User, password=var.Mysql_Password, host=var.Mysql_Host, database=var.Mysql_Database
        )
    else:
        print(err)
        
    pass

################## This function will return the total number of rows on item_list table ##################
def get_max_row():
    my_cursor = mydb.cursor()
    query = "SELECT COUNT(*) FROM item_list;"
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    result = result[0][0]
    return result

################## This function will return all data with serial no from item_list table ##################
def select_all():
    my_cursor = mydb.cursor()
    # query with serial no
    query = 'SELECT (@sno := @sno + 1) as Sno, id, item_name, item_price FROM item_list, (SELECT @sno := 0) as ini;'
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    return result

################## This function will return all data with serial no from selected_lites table ##################

def select_all_selected():
    my_cursor = mydb.cursor()
    query = "SELECT (@sno := @sno + 1) as Sno, id, item_id, selected_item_name, qty, price FROM selected_items, (SELECT @sno := 0) as ini;"
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    return result

################## This function will add new item on item_list table ###################################################
def insert_data(item_name, item_price):
    my_cursor = mydb.cursor()
    query = f"INSERT INTO item_list(item_name, item_price) VALUES('{item_name}', {item_price})"
    my_cursor.execute(query)
    mydb.commit()
    print("item inserted [OK]")

################## This function to edit the existed data on item_list table ##################
def edit_data(id, item_name, item_price):
    my_cursor = mydb.cursor()
    query1 = f"UPDATE item_list SET item_name='{item_name}' WHERE id={id};"
    query2 = f"UPDATE item_list SET item_price={item_price} WHERE id={id};"

    try:
        if item_name == '':
            pass
        else:
            my_cursor.execute(query1)
    except:
        pass

    try:
        if type(item_price) != float:
            pass
        my_cursor.execute(query2)
    except:
        pass

    mydb.commit()
    print("item modified [OK]")

################## This function will delete an item by given id in item_list table ##################
def delete_data(id):
    my_cursor = mydb.cursor()
    query = f"DELETE FROM item_list WHERE id={id}"
    my_cursor.execute(query)
    print("data deleted [OK]")
    pass

################## This function will select the items for bill ##################
def selected_id(id, qty):
    my_cursor = mydb.cursor()
    query = f"SELECT * FROM item_list WHERE id={id}"
    my_cursor.execute(query)
    result = my_cursor.fetchall()

    item_id = result[0][0]
    item_name = result[0][1]
    price = result[0][2]
    total_price = price * qty

    try:
        query2 = f"INSERT INTO selected_items(item_id, selected_item_name, qty, price) VALUES({item_id},'{item_name}',{qty},{total_price})"
        my_cursor.execute(query2)
        mydb.commit()
    except:
        print("can't do!")
        pass

################## This function will return the sum of price column in selected_items table ##################
def total_price():
    my_cursor = mydb.cursor()
    query = f"SELECT SUM(price) FROM selected_items;"
    my_cursor.execute(query)
    total = my_cursor.fetchall()
    total = total[0][0]
    return total

################## This function will delete the entry by given id in selected_items table ##################
def delete_selection(post_id):
    my_cursor = mydb.cursor()
    query = f"DELETE FROM selected_items WHERE id={post_id};"
    my_cursor.execute(query)
    print("data deleted [OK]")
    mydb.commit()

################## This function will delete all the data from selected_items table ##################
def delete_all_selected_items():
    my_cursor = mydb.cursor()
    query = "DELETE FROM selected_items;"
    my_cursor.execute(query)
    mydb.commit()

################## This function will store the purchase logs on logs table ##################
def selected_logs():
    date_ = datetime.datetime.now()
    date_ = date_.strftime("%Y-%m-%d %X")
    my_cursor = mydb.cursor()

    result = select_all_selected()
    for i in result:
        selected_item_id = i[1]
        selected_item_qty = i[4]
        price = i[5]
        query = f"INSERT INTO logs(selected_item_id,selected_qty,price,date_time) VALUES({selected_item_id},{selected_item_qty},{price},'{date_}');"
        my_cursor.execute(query)
        mydb.commit()
        print(i[0], i[1], i[2], i[3], i[4], i[5])


if __name__ == '__main__':
    pass
