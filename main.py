from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html', title="Signup")



@app.route("/welcome", methods=['post'])
def welcome():
    name_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    email = request.form["email"]
    username = request.form["username"]

    if len(username) < 3 or len(username) > 20:
        username = ""
        password = ""
        name_error = "You have entered an invalid name. A valid name has between 3 and 20 characters."
        return render_template("index.html", name_error=name_error, email=email) 

    password = request.form["password"]
    if len(password) < 3 or len(password) > 20:
        password = ""
        verifypassword = ""
        password_error = "You have entered an invalid password. A valid password has between 3 and 20 characters. Please try again."
        return render_template("index.html", username=username, email=email, password_error=password_error) 


    verifypassword = request.form["verify_password"]
    if verifypassword != password:
        verifypassword = ""
        password = ""
        verify_error = "Password does not match. Please try again."
        return render_template("index.html", username=username, email=email, verify_error=verify_error)

    if email  

    if not name_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", username=username)

app.run()