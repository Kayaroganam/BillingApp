import re
from unittest import result
import mysql.connector

DB_USER = 'kayar'
DB_PASSWORD = 'kayar@123'
DB_HOST = 'localhost'
DB = 'StationeryItems'

item_list = mysql.connector.connect(
    user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB
)

print(item_list)

#Function to count number of rows in item_list table
def get_max_row():
    my_cursor = item_list.cursor()
    query = "SELECT COUNT(*) FROM item_list;"
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    result = result[0][0]
    return result

#Function to list All data from item_list
def select_all():
    my_cursor = item_list.cursor()
    #query with serial no
    query = 'SELECT (@sno := @sno + 1) as Sno, id, item_name, item_price FROM item_list, (SELECT @sno := 0) as ini;'
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    return result

#Function to list all data from selected_items  
def select_all_selected():
    my_cursor = item_list.cursor()
    query = "SELECT (@sno := @sno + 1) as Sno, id, item_id, selected_item_name, qty, price FROM selected_items, (SELECT @sno := 0) as ini;"
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    return result

#Function to add new data
def insert_data(item_name, item_price):
    my_cursor = item_list.cursor()
    query = f"INSERT INTO item_list(item_name, item_price) VALUES('{item_name}', {item_price})"
    my_cursor.execute(query)
    item_list.commit()
    print("item inserted [OK]")

#Function to edit the exist data
def edit_data(id, item_name, item_price):
    my_cursor = item_list.cursor()
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

    item_list.commit()
    print("item modified [OK]")

#Function to delete data
def delete_data(id):
    my_cursor = item_list.cursor()
    query = f"DELETE FROM item_list WHERE id={id}"
    my_cursor.execute(query)
    print("data deleted [OK]")
    pass

#Function to create selected list
def selected_id(id, qty):
    my_cursor = item_list.cursor()
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
            item_list.commit()
    except:
        print("can't do!")
        pass

def total_price():
    my_cursor = item_list.cursor()
    query = f"SELECT SUM(price) FROM selected_items;"
    my_cursor.execute(query)
    total = my_cursor.fetchall()
    total = total[0][0]
    return total

#Function to delete selected_list data
def delete_selection(id):
    my_cursor = item_list.cursor()
    query = f"DELETE FROM selected_items WHERE id={id};"
    my_cursor.execute(query)
    print("data deleted [OK]")

#Function to delete all from selected_items
def delete_all_selected_items():
    my_cursor = item_list.cursor()
    query = "DELETE * FROM"

if __name__ == '__main__':
    print(total_price())
