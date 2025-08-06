from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'rohan_ece'
mysql = MySQL(app)

@app.route('/index.html')
def index():
    sql = "SELECT * FROM people"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return render_template("index.html",results=results)
#------------------------------


# @app.route("/index.html",methods=["GET"])
# def index():
#     return render_template("index.html")

@app.route("/about-us.html",methods=["GET"])
def about():
    return render_template("about-us.html")

@app.route("/products.html",methods=["GET"])
def product():
    return render_template("products.html")

@app.route("/contact-us.html",methods=["GET"])
def contact():
    return render_template("contact-us.html")

@app.route("/single-post.html",methods=["GET"])
def post():
    return render_template("single-post.html")




if __name__ == 'main':
    app.rum()

