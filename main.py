from flask import Flask,render_template,request,redirect,session,send_from_directory
from business.logic import checkUserPass
import os
import dotenv
import json

dotenv.load_dotenv()
app = Flask(__name__,template_folder="./templates")
app.secret_key = os.getenv("COOKIES_SECRET_KEY")   

@app.route("/",methods = ['GET','POST'])
def index():
    error = False
    with open("textsEsp.json", "r") as f:
            text = json.loads(f.read())
    if request.method == 'GET': 
        return render_template("login.html",error=error, text=text)
    if request.method == 'POST':
        user = request.form["username"]
        pwd = request.form["password"]
        if checkUserPass(user,pwd) == True:
            session['logged_in'] = True
            session['user'] = user
            return redirect("/welcome")
        else:
            error = True
            return render_template("login.html",error=error, text=text)

@app.route("/welcome",methods = ['GET'])
def welcome():
    try:
        if session['logged_in'] == True:
            welcomeText =  session['user']
            with open("accounts.json", "r") as f:
                accounts = json.loads(f.read())
            return render_template("welcome.html",welcomeText=welcomeText, accounts=accounts)
        else:
            return redirect("/")
    except KeyError:
        return redirect("/")

@app.route("/logout",methods = ['GET'])
def logout():
    session['logged_in'] = False
    return redirect("/")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )
if __name__ == '__main__':
    app.run(debug=True,host='localhost',port = 8000)

