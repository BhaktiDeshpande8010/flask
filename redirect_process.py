from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("homepage"))

@app.route("/homepage")
def homepage():
    return "This is Homepage"



if __name__=="__main__":
    app.run(debug=True)