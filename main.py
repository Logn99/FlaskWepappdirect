from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")  # this sets the route to this page
def home():
	return render_template("index.html")  

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/login", methods=["POST", "GET"])

def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr = user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"