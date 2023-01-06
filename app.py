import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///budgetwise.db")

# Make sure API key is set
#if not os.environ.get("API_KEY"):
    #raise RuntimeError("API_KEY not set")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")
            return redirect('/index')

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return redirect('/index')

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("invalid username and/or password")
            return redirect('/index')

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        email = request.form.get("email")
        # Make sure the user enter their username
        if not email:
            flash("Please enter a valid email")
            return redirect('/index')
        if not username:
            flash("Please enter a valid user name")
            return redirect('/index')
        # Make sure the user enter their password
        if not password:
            flash("Please enter a valid password")
            return redirect('/index')
        # Require users’ passwords to have some number of letters, numbers, and/or symbols.
        lower_case = 0
        upper_case = 0
        special_character = 0
        for p in range(len(password)):
            if password.islower():
                lower_case += 1
            if password.isupper():
                upper_case += 1
            if password == '@' or password == '$':
                special_character += 1
        if lower_case > 1 or upper_case > 1 or special_character > 1:
            flash("Password must contain at least a lower case character, or a upper case character, or a special character")
            return redirect('/index')
        # Make sure the user confirm their password
        elif not confirmation:
            flash("Please confirm your password")
            return redirect('/index')
        # Make sure the password and password confirmation match
        elif password != confirmation:
            flash("Password does not match")
            return redirect('/index')
        # Make sure the username that they entered do match match a user in the database
        rows = db.execute("SELECT id FROM users WHERE username = ?", username)
        if len(rows) != 0:
            flash("Username is already taken")
            return redirect('/index')

        # Add username and hash into the database
        hash = generate_password_hash(password)
        new_user = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        session["user_id"] = new_user

        return redirect('/login')

@app.route('/index')
@app.route('/')
def index():
    """Display what the website is going to be about"""
    return render_template('index.html')

@app.route("/logexpenses", methods = ["GET", "POST"])
def logexpenses():
    """Display the log expenses about"""
    if request.method == "GET":
        return render_template("logexpenses.html")
    else:
        description = request.form.get("description")
        amount = request.form.get("amount")
        category = request.form.get("category")
        date = request.form.get("date")
        expense = request.form.get("expense")

        before = db.execute("SELECT amount FROM spendings WHERE user_id= ? AND category = ?", session["user_id"], category)
        if not before:
            db.execute("INSERT INTO spendings (user_id, description, amount, category, expense, date) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], description, amount, category, expense, date)
        else:
            db.execute("UPDATE spendings SET amount = amount + ? where user_id = ? AND category = ?", amount, session["user_id"], category)
            #get new description
            old_description = db.execute("SELECT description FROM spendings where user_id= ? AND category = ?", session["user_id"], category)
            new_description = old_description[0]["description"] + ", " + description
            db.execute("UPDATE spendings SET description = ? where user_id = ? AND category = ?", new_description, session["user_id"], category)
        return redirect("/history")

@app.route("/analytics", methods = ["GET"])
@login_required
def analytics():
    if request.method == "GET":
        # Make it work even when some categories are empty (check this, or start table with 0 in every category)
        # Right now, running 7 SELECTs -> find more efficient way to do it (can do this after most of project is complete)
        spendings = {}
        resultsHousing = db.execute("SELECT category, amount FROM spendings WHERE user_id= ? AND category = 'housing'", session["user_id"])
        if resultsHousing:
            spendings["housing"] = resultsHousing[0]["amount"]
        else:
            flash("Please enter input for housing")
            return redirect("/logexpenses")

        resultsTransportation = db.execute("SELECT category, amount FROM spendings WHERE user_id= ? AND category = 'transportation'", session["user_id"])
        if resultsTransportation:
            spendings["transportation"] = resultsTransportation[0]["amount"]
        else:
            flash("Please enter input for transporation")
            return redirect("/logexpenses")

        resultsFood = db.execute("SELECT category, amount FROM spendings WHERE user_id= ? AND category = 'food'", session["user_id"])
        if resultsFood:
            spendings["food"] = resultsFood[0]["amount"]
        else:
            flash("Please enter input for food")
            return redirect("/logexpenses")

        resultsUtilities = db.execute("SELECT category, amount FROM spendings WHERE user_id= ? AND category = 'utilities'", session["user_id"])
        if resultsUtilities:
            spendings["utilities"] = resultsUtilities[0]["amount"]
        else:
            flash("Please enter input for utilities")
            return redirect("/logexpenses")

        resultsInsurance = db.execute("SELECT category, amount FROM spendings WHERE user_id= ? AND category = 'insurance'", session["user_id"])
        if resultsInsurance:
            spendings["insurance"]= resultsInsurance[0]["amount"]
        else:
            flash("Please enter input for insurance")
            return redirect("/logexpenses")

        resultsPersonalSpending = db.execute("SELECT category, amount FROM spendings WHERE user_id= ? AND category = 'personalspending'", session["user_id"])
        if resultsPersonalSpending:
            spendings["personalspending"] = resultsPersonalSpending[0]["amount"]
        else:
            flash("Please enter input for personal spending")
            return redirect("/logexpenses")

        resultsSaving = db.execute("SELECT category, amount FROM spendings WHERE user_id= ? AND category = 'saving'", session["user_id"])
        if resultsSaving:
            spendings["saving"] = resultsSaving[0]["amount"]
        else:
            flash("Please enter input for saving")
            return redirect("/logexpenses")

        categories = {}
        totalSave = db.execute("SELECT expense, SUM(amount) as total FROM spendings WHERE user_id= ? GROUP BY expense", session["user_id"])

        print(totalSave)

        return render_template("analytics.html", spendings=spendings, categories=totalSave)

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    histories = db.execute("SELECT description, amount, category, expense, date FROM spendings WHERE user_id= ?", session["user_id"])
    return render_template("history.html", histories=histories)

@app.route("/calculator")
@login_required
def calculator():
    return render_template("calculator.html")
