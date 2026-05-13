from flask import *
app=Flask(__name__)      #helps to run a particular file

@app.route("/")
def home():
    return "URL building task"


# string value 
@app.route("/name/<value>")
def name(value):
    return "my name is %s" %value


# integer value 
@app.route("/rollno/<int:num>")
def rollno(num):
    return "my roll number is %s" %num

if __name__=="__main__":
    app.run(debug=True)