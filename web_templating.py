from flask import *

app = Flask(__name__)   # helps to run a particular file

# BASIC FILE RENDERING 
@app.route("/")
def home():
    # student_list=[12,34,'hello',67, True]
    student_list={1:200,2:300,3:400,4:500,6:700}
    return render_template("home.html",s_list=student_list)


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