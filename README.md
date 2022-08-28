# BillingApp

## Installation on Ubuntu

```
sudo apt update -y
sudo apt install python3 python3-pip -y
sudo pip3 install flask mysql-connector-python
sudo apt install mysql-server -y
sudo systemctl enable --now mysqld.service
sudo ufw allow 3306/tcp
sudo ufw allow 5000/tcp
sudo ufw reload
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
sudo systemctl enable --now mysqld.service
sudo firewall-cmd --permanent --add-port=3306/tcp
sudo firewall-cmd --permanent --add-port=5000/tcp
sudo firewall-cmd --reload
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

## Automatic Installation script
```
git clone https://github.com/Kayaroganam/shell_script.git
bash shell_script/Deploy_Billing_App.sh
```
