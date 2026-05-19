from flask import *               
app=Flask(__name__)                              

@app.route("/")
def home():
    return "<h1>Hello Flask</h1>"


@app.route("/register")
def register():
    return render_template("reg.html")


@app.route("/about")
def service():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)