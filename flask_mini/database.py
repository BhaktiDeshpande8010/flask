import sqlite3 as sq
con=sq.connect("Flask.db")
cur=con.cursor()

import sqlite3 as sq

con = sq.connect("Flask.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE registration(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    email VARCHAR(20),
    password VARCHAR(20),
    contact VARCHAR(15)
)
""")

cur.execute("insert into registration(name,email,password,contact) values(?,?,?,?)",('ram','ram@gmail.com','1234','54669854'))


con.commit()
con.close()