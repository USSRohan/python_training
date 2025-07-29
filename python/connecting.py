import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="rohan_ece"
        )


mycursor = mydb.cursor()
mycursor.execute("select * from user")

result = mycursor.fetchall()
for row in result:
    print(row)


mydb.commit()

mycursor.close()
mydb.close()
# print(mycursor.rowcount, "record insterted")


