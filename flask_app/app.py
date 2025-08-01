from flask import Flask,render_template

app = Flask(__name__)
# ------------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/')
def hello_world():
    return 'Hello world!!!'

@app.route('/notMyName')
def printMyname():
    return 'Your Name'
# ------------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/HOME')
def printHomeHTML():
    return render_template("home.html")

@app.route('/ABOUT')
def printAbout():
    return render_template("home_about.html")

@app.route('/CONTACT')
def printContact():
    return render_template("home_contact.html")



if __name__ == '__main__':
    app.run()

