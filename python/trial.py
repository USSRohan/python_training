import mysql.connector

def insert_data(id, name, email, phone):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="rohan_ece"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO user(id, name, email, phone) VALUES (%s, %s, %s, %s)"
    val = [id, name, email, phone]
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted")

    mycursor.close()
    mydb.close()

id = input("Enter ID: ")
name = input("Enter Name: ")
email = input("Enter Email: ")
phone = input("Enter Phone Number: ")

insert_data(id, name, email, phone)
