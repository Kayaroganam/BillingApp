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

sudo apt install git
sudo git clone https://github.com/Kayaroganam/BillingApp.git /opt/BillingApp
sudo vim /opt/BillingApp/variables.py
sudo python3 /opt/BillingApp/run.py
```
