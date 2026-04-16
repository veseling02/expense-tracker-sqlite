from flask import Flask, render_template, request, redirect, url_for
import database as db
from datetime import datetime


app = Flask(__name__)

@app.route("/")

def index():
    transactions = db.get_all_trans()
    total = round(sum(t.amount for t in transactions), 2)
    print(f"DEBUG: Found {len(transactions)} transactions")

    return render_template("index.html", trans_list=transactions, balance=total)

@app.route("/add", methods=["POST"])
def handle_add():
    tx_type = request.form.get("tx_type")
    categ = request.form.get("categ_name")
    amount = float(request.form.get("amount_val"))
    today = datetime.now().strftime("%d-%m-%Y")

    if tx_type == "Expense":
        amount = -abs(amount)
    
    db.create_transaction(tx_type, categ, amount, today)

    return redirect(url_for("index"))

@app.route("/delete/<int:transaction_id>")
def handle_delete(transaction_id):
    db.delete_transaction(transaction_id)
    return redirect(url_for("index"))

@app.route("/clear-all")
def handle_clear():
    db.clear_all()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()