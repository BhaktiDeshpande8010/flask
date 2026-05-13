from flask import *               
app=Flask(__name__)                              

# @app.route("/")
# def home():
#     return "<h1>Hello Flask</h1>"


# @app.route("/about")
# def about():
#     return "I'm about page"


# @app.route("/service")
# def service():
#     return "<b>This is service page</b>"

# @app.route("/gallery")
# def gallery():
#     return "<i>This is gallery page</i>"

# if __name__=="__main__":
#     app.run(debug=True)



# BASIC FILE RENDERING 
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/service")
def service():
    return "<b>This is service page</b>"

@app.route("/contact")
def gallery():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)