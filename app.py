from flask import Flask, render_template
from database import get_all_trans

app = Flask(__name__)

@app.route("/")

def index():
    transactions = get_all_trans()
    total = sum(t.amount for t in transactions)
    print(f"DEBUG: Found {len(transactions)} transactions")

    return render_template("index.html", trans_list=transactions, balance=total)



if __name__ == "__main__":
    app.run()