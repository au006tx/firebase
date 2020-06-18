import MySQLdb

db = MySQLdb.connect("localhost","root","alpine1234","new")
cursor = db.cursor()

query = ("show databases")

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()