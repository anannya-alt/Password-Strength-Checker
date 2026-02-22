from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&*]", password):
        score += 1

    percentage = (score / 5) * 100

    if score <= 2:
        return "Weak", percentage
    elif score == 3 or score == 4:
        return "Medium", percentage
    else:
        return "Strong", percentage

@app.route("/", methods=["GET", "POST"])
def index():
    strength = ""
    percentage = 0

    if request.method == "POST":
        password = request.form["password"]
        strength, percentage = check_password_strength(password)

    return render_template("index.html", strength=strength, percentage=percentage)

if __name__ == "__main__":
    app.run(debug=True)