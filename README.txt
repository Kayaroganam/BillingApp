#Installation

  1. Step 1: Download and install Python3
    i. link: https://www.python.org/downloads/
  
  2. Step 2: Install some python modules
    i.  Open terminal.
    ii. type the command "pip install flask, mysql-connector-python" the hit Enter.
  
  3. Step 3: Download and install MySQL server
    i. https://www.mysql.com/downloads/ (or) open terminal type the command "sudo apt install mysql-server" then hti Enter.
  
  4. Step 4: Configure the database
    i. Execute the given commands line by line.
      $ sudo mysql
      mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
      mysql> GRANT PRIVILEGE ON database.table TO 'username'@'localhost';
      mysql> FLUSH PRIVILEGES;
      mysql> CREATE DATABASE StationeryItems;
      mysql> USE StationeryItems;
      mysql> CREATE TABLE item_list(id INT NOT NULL AUTO_INCREMENT, item_name VARCHAR(255) NOT NULL, item_price FLOAT NOT NULL, PRIMARY KEY(id));
      mysql> CREATE TABLE selected_items(id INT NOT NULL AUTO_INCREMENT, item_id INT NOT NULL, qty FLOAT NOT NULL, price FLOAT NOT NULL, PRIMARY KEY(id));
      mysql> ALTER TABLE selected_items ADD selected_item_name VARCHAR(255) NOT NULL AFTER item_id;
      mysql> CREATE TABLE logs(id INT NOT NULL AUTO_INCREMENT, selected_item_id INT NOT NULL, selected_qty FLOAT NOT NULL,price FLOAT,date_time DATETIME, PRIMARY KEY(id));
  
  5. Step 5: Download the Repository
    i. link : https://github.com/Kayaroganam/StationeryItems 
      (or) 
      open terminal type the command git clone https://github.com/Kayaroganam/StationeryItems.git then hit Enter.
  
  6. Step 6: make some changes on database_operation.py file
    i. Navigate to the downloaded repository and open database_operation.py using an editor.
    ii. Find some lines like 
      DB_USER = 'kayar'  #change kayar to your mysql user which is you created just now
      DB_PASSWORD = 'kayar@123' #change kayar@123 to your mysql password
      DB_HOST = 'localhost'
      DB = 'StationeryItems'
  
  7. Step 7: Run run.py file
    i. Open terminal and type "python3 run.py" then hit Enter.
    ii. if you are using windows system open cmd and type "python run.py" then hit Enter.
    
  8. Step 8: open the website
  i. Open your web browser.
  ii. type "127.0.0.1:5000" on serach bar then hit Enter.
  
  
  Now your billing software is ready.
