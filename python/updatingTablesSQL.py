import mysql.connector

def update_people(id,name):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="rohan_ece"
            )


    mycursor = mydb.cursor()
    sql = "UPDATE people SET name = %s where id = %s"
    val = [name,id]
    mycursor.execute(sql,val)


    mydb.commit()
    print(mycursor.rowcount,"record updated.")
    mycursor.close()
    mydb.close()


id = input("Enter the user ID to update: ")
name = input("Enter the NEW NAME: ")
update_people(id,name)