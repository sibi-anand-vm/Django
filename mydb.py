#mydb.py
import mysql.connector
database=mysql.connector.connect(
host='localhost',
user='root',
password='ACCESS_LOCk42'

)
cursor=database.cursor()
cursor.execute('create database crm')
print("All done here")