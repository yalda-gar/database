from flask import Flask, render_template, request
import sqlite3 

app = Flask(__name__)

def get_db():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection 

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)