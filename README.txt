#Installation

  1. Step 1: Download and install Python3
    i. windows: https://www.python.org/downloads/ 
    ii. ubuntu: sudo apt update -y && sudo apt install python3 python3-pip -y
  
  2. Step 2: Install some python modules
    i.  Open terminal.
    ii. type the command "sudo pip3 install flask mysql-connector-python" the hit Enter.
  
  3. Step 3: Download and install MySQL server
    i. https://www.mysql.com/downloads/ (or) open terminal type the command "sudo apt install mysql-server" then hti Enter.
  
  4. Step 4: Configure the database
    i. Execute the given commands line by line.
      $ sudo mysql
      mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
      mysql> GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
      mysql> FLUSH PRIVILEGES;
      mysql> exit
  
  5. Step 5: Download the Repository
    i. link : https://github.com/Kayaroganam/StationeryItems 
      (or) 
      open terminal type the command git clone https://github.com/Kayaroganam/StationeryItems.git then hit Enter.
  
  6. Step 6: make some changes on variables.py file
    i. Navigate to the downloaded repository and open database_operation.py using an editor.
    ii. Find some lines like given below and change to your required values.

    class var:
      Mysql_User = 'kayar'  
      Mysql_Password = 'kayar@123'
      Mysql_Database = 'StationeryItems'
      Mysql_Host = 'localhost'

      My_Email = 'kayarogan2003@gmail.com'  
      My_Email_Password = 'rxynvahxkluzqykg' 
      
      Company = 'Stationery Store' # Enter your title name

  
  7. Step 7: Run run.py file
    i. Open terminal and type "python3 run.py" then hit Enter.
    ii. if you are using windows system open cmd and type "python run.py" then hit Enter.
    
  8. Step 8: open the website
    i. Open your web browser.
    ii. type "127.0.0.1:5000" on serach bar then hit Enter.
  
  
  Now your billing software is ready.
