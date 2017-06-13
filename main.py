from flask import Flask, request, redirect, render_template
import cgi

app=Flask(__name__)
app.config['DEBUG']=True

def long_enuf(entry):
    if len(entry)>2 and len(entry)<21:
        return True

@app.route("/validate")
def validate_info():
    username=request.args['username']
    password=request.args['password']
    password_confirmation=request.args['password_confirmation']
    email=request.args['email']

    username_error=''
    password_error=''
    password_confirmation_error=''
    email_error=''
    
    if not long_enuf(username):
        username_error = "Please enter a valid username"
    if not long_enuf(password):
        password_error = "Please enter a valid password"
    if password_confirmation != password:
        password_confirmation_error = "Passwords do not match!"
    if not long_enuf(email) or not '@' in email or not '.' in email:    
    
        email_error = "Please enter a valid email"
    if not username_error and not password_error and not password_confirmation_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, password_confirmation_error=password_confirmation_error, email_error=email_error, username=username, email=email)


@app.route("/")
def index():
    return render_template('index.html')
    

app.run()

