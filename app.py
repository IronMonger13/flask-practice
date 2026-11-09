from flask import Flask

app = Flask(__name__)


# HOME
@app.route("/")
def home():
    return "<h1>Welcome</h1>"


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    return "<h1>Dashboard</h1>"


# ALL EXPENSES
@app.route("/expenses")
def expenses():
    return "<h1>Your expenses</h1>"


# ADD EXPENSES
@app.route("/add-expense")
def add_expense():
    return "<h1>Add expense</h1>"


# REGISTER USER
@app.route("/register")
def register():
    return "<h1>Register</h1>"


# LOGIN
@app.route("/login")
def login():
    return "<h1>Login</h1>"


app.run(debug=True)
