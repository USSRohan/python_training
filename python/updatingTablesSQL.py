import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="rohan_ece"
        )


mycursor = mydb.cursor()
mycursor.execute("update user set password =  123456 where email = uddhav@gmail.com")

# result = mycursor.fetchall()
# for row in result:
#     print(row)


mydb.commit()

mycursor.close()
mydb.close()
# print(mycursor.rowcount, "record insterted")


