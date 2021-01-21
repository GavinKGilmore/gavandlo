from flask import Flask, redirect, url_for, render_template, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date as d

app = Flask("__main__")
app.secret_key = "565weather4d"

@app.route("/")
def home():
	if "user" in session:
		return render_template("index.html")
		print(session["user"])
	else:
		return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
	password = "gav&lo"
	password2 = "grease"
	if "user" not in session:
		if request.method == "POST":
			user = request.form["login"]
			if user.lower() == password:
				#session.permanent = False
				#session["user"] = user
				flash("you really thought it would be that easy?")
				flash("your hint: '______ is the word' ")
				return redirect(url_for("login"))
			elif user.lower() == password2:
				session["user"] = user
				return redirect(url_for("home"))
			else:
				flash("incorrect password")
				return redirect(url_for("login"))
		return render_template("login.html")
	else:
		return redirect(url_for("home"))

@app.route("/day<num>")
def day(num):
	date = d.today()
	if "user" in session and str(date) == "2021-01-19":
		return render_template(f"day{num}.html")
	else:
		return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)
