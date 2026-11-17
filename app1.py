from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return "Home Page..."


# VIEW EXPENSE
@app.route("/expenses/<int:expense_id>")
def view_expense(expense_id):
    return f"<h1>Expense ID: {expense_id}</h1>"


with app.test_request_context():
    generated_url = url_for("view_expense", expense_id=7)
    # print(generated_url)


@app.route("/user/<string:username>/expense/<int:expense_id>")
def user_expense(username, expense_id):
    return f"<h1>Username: {username}\nExpense ID: {expense_id}</h1>"


with app.test_request_context():
    generated_url = url_for("user_expense", username="ABC", expense_id=10)
    print(generated_url)


# DELETE EXPENSE
@app.route("/expenses/<int:expense_id>/delete", methods=["GET", "POST"])
def delete_expense(expense_id):
    return redirect(url_for("view_expense", expense_id=7))


app.run(debug=True)
