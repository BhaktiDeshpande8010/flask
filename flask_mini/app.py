from flask import *               
app=Flask(__name__)                              

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register")
def register():
    return render_template("reg.html")


@app.route("/about")
def service():
    return render_template("about.html")

@app.route("/saveform", methods=["POST", "GET"])
def saveform():
    if request.method == "POST":
        nm = request.form["name"]
        em = request.form["email"]
        ps = request.form["password"]
        cn = request.form["contact"]

        import sqlite3 as sq

        con = sq.connect("Flask.db")
        cur = con.cursor()
        cur.execute(
            "insert into registration(name,email,password,contact) values(?,?,?,?)",
            (nm, em, ps, cn)
        )
        
        con.commit()
        con.close()

        return "Registration Successful"

    else:
        return "failed"

if __name__=="__main__":
    app.run(debug=True)

