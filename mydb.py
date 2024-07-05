import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rubel@2020",
)

# prepare a cursor object using cursor() method
cursor = dataBase.cursor()

# Create database
cursor.execute("CREATE DATABASE storefront")

print("Database created successfully")