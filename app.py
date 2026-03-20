from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return "<i>Welcome to</i> <b>discuss</b>!"
