import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="123456",database="db_zaid")

cursor = db.cursor()

cursor.execute("SELECT CURRENTUSER()")

data = cursor.fetchmany()
print("Database version : %s " % data)

db.close()