import sqlite3 as sq

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
    

@app.route("/viewdata")
def viewdata():
    con=sq.connect("Flask.db")
    cur=con.cursor()
    cur.execute("Select * from registration order by id desc")
    data=cur.fetchall()

    con.commit()
    con.close()
    return render_template("viewdata.html",s_data=data)  #this data is like an variable the entire data from db is going to get store in it 
                                                        #and the s_data is also an variable which we will use in html page,so that data will be visible there


if __name__=="__main__":
    app.run(debug=True)

