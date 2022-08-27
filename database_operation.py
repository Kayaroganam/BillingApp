import os
import mysql.connector
from mysql.connector import errorcode
import datetime
from variables import var

try:
    item_list = mysql.connector.connect(
        user=var.Mysql_User, password=var.Mysql_Password, host=var.Mysql_Host, database=var.Mysql_Database
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access Denied!")

    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Datase doesn't exist!")
        print("Creating database ...")
        os.system(f'mysql -u {var.Mysql_User} -p{var.Mysql_Password} < database_structure.sql')
        
        item_list = mysql.connector.connect(
        user=var.Mysql_User, password=var.Mysql_Password, host=var.Mysql_Host, database=var.Mysql_Database
        )

    else:
        print(err)
    pass

# Function to count number of rows in item_list table


def get_max_row():
    my_cursor = item_list.cursor()
    query = "SELECT COUNT(*) FROM item_list;"
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    result = result[0][0]
    return result

# Function to list All data from item_list


def select_all():
    my_cursor = item_list.cursor()
    # query with serial no
    query = 'SELECT (@sno := @sno + 1) as Sno, id, item_name, item_price FROM item_list, (SELECT @sno := 0) as ini;'
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    return result

# Function to list all data from selected_items


def select_all_selected():
    my_cursor = item_list.cursor()
    query = "SELECT (@sno := @sno + 1) as Sno, id, item_id, selected_item_name, qty, price FROM selected_items, (SELECT @sno := 0) as ini;"
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    return result

# Function to add new data


def insert_data(item_name, item_price):
    my_cursor = item_list.cursor()
    query = f"INSERT INTO item_list(item_name, item_price) VALUES('{item_name}', {item_price})"
    my_cursor.execute(query)
    item_list.commit()
    print("item inserted [OK]")

# Function to edit the exist data


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

# Function to delete data


def delete_data(id):
    my_cursor = item_list.cursor()
    query = f"DELETE FROM item_list WHERE id={id}"
    my_cursor.execute(query)
    print("data deleted [OK]")
    pass

# Function to create selected list


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

# Function to delete selected_list data


def delete_selection(post_id):
    my_cursor = item_list.cursor()
    query = f"DELETE FROM selected_items WHERE id={post_id};"
    my_cursor.execute(query)
    print("data deleted [OK]")
    item_list.commit()

# Function to delete all from selected_items


def delete_all_selected_items():
    my_cursor = item_list.cursor()
    query = "DELETE FROM selected_items;"
    my_cursor.execute(query)
    item_list.commit()


def selected_logs():
    date_ = datetime.datetime.now()
    date_ = date_.strftime("%Y-%m-%d %X")
    my_cursor = item_list.cursor()

    result = select_all_selected()
    for i in result:
        selected_item_id = i[1]
        selected_item_qty = i[4]
        price = i[5]
        query = f"INSERT INTO logs(selected_item_id,selected_qty,price,date_time) VALUES({selected_item_id},{selected_item_qty},{price},'{date_}');"
        my_cursor.execute(query)
        item_list.commit()
        print(i[0], i[1], i[2], i[3], i[4], i[5])


if __name__ == '__main__':
    selected_logs()
    pass
