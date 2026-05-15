from flask import *

app = Flask(__name__)   # helps to run a particular file

@app.route("/about")
def about():

    name = "python"
    return render_template("about.html", studentname=name)

@app.route("/contact")
def contact():

    num = 34
    return render_template("contact.html", num1=num)

if __name__ == "__main__":
    app.run(debug=True)