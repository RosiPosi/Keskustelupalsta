from flask import Flask
import sqlite3
from flask import abort, redirect, render_template, request, session
import config
import db
import items
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def check_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_items = items.get_items()
    return render_template("index.html", items=all_items)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_item(item_id)
    if not item:
        abort(404)
    return render_template("show_item.html", item=item)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    items = users.get_item(user_id)
    return render_template("show_user.html", user=user, items=items)

# POSTING / EDITING

@app.route("/new_item")
def new_item():
    check_login()
    return render_template("new_item.html")

@app.route("/create_item", methods=["POST"])
def create_item():
    check_login()

    title = request.form["title"]
    description = request.form["description"]
    user_id = session["user_id"]

    if not title or len(title) > 50:
        abort(403)
    if len(description) > 1000:
        abort(403)

    items.add_item(title, description, user_id)

    return redirect("/")

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item[ "user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_item.html", item=item)

@app.route("/update_item", methods=["POST"])
def update_item():
    item_id = request.form["item_id"]

    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item[ "user_id"] != session["user_id"]:
        abort(403)
        
    title = request.form["title"]
    description = request.form["description"]

    if not title or len(title) > 50:
        abort(403)

    items.update_item(item_id, title, description)

    return redirect("/item/" + str(item_id))

@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item[ "user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)
    
    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))
        
# SEARCHING
@app.route("/search")
def search():
    query = request.args.get("query")
    if query:
        results = items.search_results(query)
    else:
        query = ""
        results = []
    return render_template("search_results.html", query=query, results=results)

# REGISTRATION AND LOGGING IN / USER RELATED CODE

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "ERROR: passwords don't match."
    
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "ERROR: username already taken."

    return "Account created! Return to the main page to log in."


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":      
        username = request.form["username"]
        password = request.form["password"]

    user_id = users.check_login(username, password)
    if user_id:
        session["user_id"] = user_id
        session["username"] = username
        return redirect("/")
    else:
        return "ERROR: wrong username or password."

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")