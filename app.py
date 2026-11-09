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


# VIEW EXPENSE
@app.route("/expenses/<int:expense_id>")
def view_expense(expense_id):
    return f"<h1>Expense ID: {expense_id}</h1>"


# ADD EXPENSES
@app.route("/add-expense", methods=["POST"])
def add_expense():
    return "<h1>Add expense</h1>"


# EDIT EXPENSE
@app.route("/expenses/<int:expense_id>/edit", methods=["POST"])
def edit_expense(expense_id):
    return f"<h1>Edit Expense with ID: {expense_id}</h1>"


# DELETE EXPENSE
@app.route("/expenses/<int:expense_id>/delete", methods=["POST"])
def delete_expense(expense_id):
    return f"<h1>Delete Expense with ID: {expense_id}</h1>"


# FILTER EXPENSE BY CATEGORY
@app.route("/expenses/category/<string:category_name>")
def expenses_by_category(category_name):
    return f"<h1>Expenses in {category_name}</h1>"


# REGISTER USER
@app.route("/register")
def register():
    return "<h1>Register</h1>"


# LOGIN
@app.route("/login")
def login():
    return "<h1>Login</h1>"


app.run(debug=True)
