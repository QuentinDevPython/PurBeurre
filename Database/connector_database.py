import mysql.connector


database = mysql.connector.connect(
    host="localhost", user="root", password="EMQG1371#psh9114S"
)

cur = database.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS purBeurre")
