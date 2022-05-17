import sqlite3

# conn=psycopg2.connect(database='userDB',user='app1',password='app@123',host='fac2133',
#                      port=5432)
conn=sqlite3.connect('ericcson.db')
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE employee(empid REAL,emp_name REAL,tech REAL)")

def load_data():
    eid=int(input("Enter your empid:"))
    ename=input("Enter your name:")
    etech=input("Enter the tech name:")
    #c.execute("INSERT INTO employee VALUES(1001,'Arun VetriMarana','Java')")
    c.execute("INSERT INTO employee VALUES(?,?,?)",(eid,ename,etech))
    conn.commit()

def update_data():
    c.execute("UPDATE employee SET tech='Python' WHERE tech='Java'")

def delete_data():
    c.execute("DELETE FROM employee WHERE empid=1004")
def get_data():
    c.execute("SELECT * FROM employee")
    #fetchone, fetchmany, fetchall
    #print(c.fetchone())
    #print(c.fetchmany(5))
    for row in c.fetchall():
        print(row[1])
#create_table()
# for x in range(5):
#     load_data()
#update_data()
#delete_data()
get_data()
conn.commit()
c.close()
conn.close()