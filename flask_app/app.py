from flask import Flask,render_template,jsonify,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'rohan_ece'
mysql = MySQL(app)

# ------------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/')
def hello_world():
    return 'Hello world!!!'

@app.route('/notMyName')
def printMyname():
    return 'Your Name'
# ------------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/HOME')
def printHome():
    return render_template("home.html")

@app.route('/ABOUT')
def printAbout():
    return render_template("home_about.html")

@app.route('/CONTACT')
def printContact():
    return render_template("home_contact.html")

@app.route('/user_details')
def userData():
    sql = "SELECT * FROM people"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return jsonify (results)
#--------------------------------------------------------------------------------------------------------------------------------------------------

# @app.route('/user_details')
# def userData():
#     id = request.args.get("id")
#     sql = ""
#     if id is None:
#         sql = "SELECT * FROM people"
#     else: 
#         sql = f"SELECT * FROM people where id = {id}"

#     cur = mysql.connection.cursor()
#     cur.execute(sql)
#     results = cur.fetchall()
#     cur.close()
#     return jsonify (results)

@app.route("/add",methods=["POST"])
def addUser():
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    

    cur = mysql.connection.cursor()
    sql = "insert into people(id,name,email,password)values(%s,%s,%s,%s)"
    val = [id,name,email,password]

    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()

    return "register success"

@app.route("/register",methods=["GET"])
def register():
    return render_template("register.html")
#----------------------------------------------------------------------------------------------------------------------------------------
@app.route("/update",methods=["POST"])
def updateUser():
    id = request.form['id']

    email = request.form['email']

    cur = mysql.connection.cursor()
    sql = "update people set email = %s where id = %s"
    # sql = "update people (id,name,email,password)values(%s,%s,%s,%s)"
    val = [email,id]

    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()
    return "register success"

    
@app.route("/updates",methods=["GET"])
def update():
    return render_template("update.html")
#-----------------------------------------------------------------------------------------------------------------------------------------
@app.route("/delete",methods=["POST"])
def deleteUser():
    id = request.form['id']

    cur = mysql.connection.cursor()
    sql = "DELETE FROM people WHERE id = %s"
    val = [id]

    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()
    return "register success"


@app.route("/deleting",methods=["GET"])
def delete():
    return render_template("delete.html")

#----------------------------------------------------------------------------------------------------------------------------------------
@app.route("/myweb",methods=["GET"])
def myweb():
    return render_template("index.html")

#----------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()

