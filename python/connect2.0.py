import mysql.connector

def insert_data(id,name,email,phone):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="rohan_ece"
            )
# print("connected to the data base: seccess")


    mycursor = mydb.cursor()

    # result = mycursor.fetchall()
    # for row in result:
    #     print(row)


    sql = "INSET INTO user(id,name,email,phone) VALUES (%s,%s,%s,%s)"
    val = [id, name, email,phone]
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record insterted")
    mycursor.close()
    mydb.close()

id = input("enter id: ")
name = input("enter the name: ")
email = input("enter the email: ")
phone = input("enter phone number: ")
insert_data(id,name,email,phone)