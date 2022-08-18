#Installation

  1. Step 1: Download and install Python3
  i. link: https://www.python.org/downloads/
  
  2. Step 2: Install some python modules
  i.  Open terminal.
  ii. type the command "pip install flask, mysql-connector-python" the hit Enter
  
  3. Step 3: Download and install MySQL server
  i. https://www.mysql.com/downloads/ (or) open terminal type the command "sudo apt install mysql-server"
  
  4. Step 4: Configure the database
  i. Execute the given commands line by line
  $ sudo mysql
  mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
  mysql> GRANT PRIVILEGE ON database.table TO 'username'@'localhost';
  mysql> FLUSH PRIVILEGES;
  mysql> CREATE 
