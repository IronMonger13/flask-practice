from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome</h1>"


@app.route("/dashboard")
def dashboard():
    return "<h1>Dashboard</h1>"


@app.route("/expenses")
def expenses():
    return "<h1>Your expenses</h1>"


@app.route("/add_expense")
def add_expense():
    if request.method == "POST":
        return "Expense saved"
    return "<h1>Add expense</h1>"


@app.route("/register")
def register():
    return "<h1>Register</h1>"


@app.route("/login")
def login():
    return "<h1>Login</h1>"


app.run(debug=True)
