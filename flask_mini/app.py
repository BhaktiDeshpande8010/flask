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
                                          

@app.route("/deletestudent/<int:id>")
def deletestudent(id):
    con=sq.connect("Flask.db")
    cur=con.cursor()
    cur.execute("delete from registration where id=?",[id])
    data=cur.fetchall()

    con.commit()
    con.close()
    return redirect(url_for("viewdata"))


@app.route("/updatestudent/<int:id>")
def updatestudent(id):
    con=sq.connect("Flask.db")
    cur=con.cursor()
    cur.execute("select * from registration where id=?", [id])
    data = cur.fetchone()
    
    con.commit()
    con.close()
    return render_template("update.html",data=data)


# @app.route("/profileupdate",methods=["POST","GET"])
# def profileupdate():
#     if request.method=="POST":
#         nm = request.form["name"]
#         em = request.form["email"]
#         ps = request.form["password"]
#         cn = request.form["contact"]
        
#         con = sq.connect("Flask.db")
#         cur = con.cursor()
#         cur.execute("update registration set name=?,email=?,password=?,contact=? where id=?",(nm,em,ps,cn,id))
        
#         con.commit()
#         con.close()
        
#         return redirect("viewdata.html")

@app.route("/profileupdate", methods=["POST", "GET"])
def profileupdate():
    if request.method == "POST":

        id = request.form["id"]   # get hidden id field
        nm = request.form["name"]
        em = request.form["email"]
        ps = request.form["password"]
        cn = request.form["contact"]

        con = sq.connect("Flask.db")
        cur = con.cursor()

        cur.execute(
            "update registration set name=?, email=?, password=?, contact=? where id=?",
            (nm, em, ps, cn, id)
        )

        con.commit()
        con.close()

        return redirect(url_for("viewdata"))
        
        

if __name__=="__main__":
    app.run(debug=True)

