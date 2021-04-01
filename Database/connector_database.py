import mysql.connector


database = mysql.connector.connect(
    host="localhost", user="root", password="your_password"
)

cur = database.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS purBeurre")
