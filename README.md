# BillingApp

## Installation on Ubuntu

```
sudo apt update -y
sudo apt install python3 python3-pip -y
sudo pip3 install flask mysql-connector-python
sudo apt install mysql-server -y

sudo mysql
mysql> CREATE USER 'kayar'@'localhost' IDENTIFIED BY 'kayar';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'kayar'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> exit

mysql -u kayar -pkayar < database_structure.sql

sudo apt install git
sudo git clone https://github.com/Kayaroganam/BillingApp.git /opt/BillingApp
sudo vi /opt/BillingApp/variables.py
sudo python3 /opt/BillingApp/run.py
```

## Installation on Centos

```
sudo dnf update -y
sudo dnf install python3 python3-pip -y
sudo pip3 install flask mysql-connector-python
sudo dnf install mysql-server -y

sudo mysql
mysql> CREATE USER 'kayar'@'localhost' IDENTIFIED BY 'kayar';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'kayar'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> exit

mysql -u kayar -pkayar < database_structure.sql

sudo dnf install git
sudo git clone https://github.com/Kayaroganam/BillingApp.git /opt/BillingApp
sudo vi /opt/BillingApp/variables.py
sudo python3 /opt/BillingApp/run.py
```

## automatic Installation script
```
git clone https://github.com/Kayaroganam/shell_script.git
bash shell_script/Deploy_Billing_App.sh
```
