import sqlite3
conn=sqlite3.connect("student_prg.db")
cur=conn.cursor()
def create_tb():
    cur.execute("create table if not exists stu(name text ,usn text primary key,mno integer,branch text)")
def insert_tb():
    name,usn,mno,branch=input("enter name usn mno branch in the same order").split()
    if usn!="NULL":
     cur.execute("insert into stu values(?,?,?,?)",(name,usn,int(mno),branch))
     conn.commit()
    else:
        print("primary ket usn can not be empty")
def delete_tb():
    opt=input("enter the usn you want do delete ")
    cur.execute("delete from stu where usn=?",(opt,))
    conn.commit()
def update_tb():
    opt=int(input(" enter the option you want to update \n1.name  \n2.mno \n3.branch \n"))
    if opt==1:
        o_name=input("enter the old name")
        n_name=input("enter the new name")
        cur.execute("update stu set name=? where name=?",(n_name,o_name))
        conn.commit()
    if opt==2:
        o=input("enter the old mobile no")
        n=input("enter the new mobile no")
        cur.execute("update stu set mno=? where mno=?",(n,o))
        conn.commit()
    if opt==3:
        o3=input("enter the old branch")
        n3_name=input("enter the new branch")
        cur.execute("update stu set branch=? where branch=?",(n3,o3))
        conn.commit()
    else:
       print("invalid option")
def display_tb():
    print("Details of all the student are: \n")
    cur.execute("select * from stu")
    t=cur.fetchall()
    for i in t:
        print(i)
def query_tb():
    opt=int(input("enter the option to see details as per :\n1.name \n2.usn\n3.mobile no\n4.branch"))
    if opt==1:
        o=input("enter the name")
        cur.execute("select * from stu where name=?",(o,))
        t=cur.fetchall()
        for i in t:
          print(i)
    if opt==2:
        u=input("enter the usn")
        cur.execute("select * from stu where usn=?",(u,))
        t=cur.fetchall()
        for i in t:
          print(i)
    if opt==3:
        m=input("enter the mobile no")
        cur.execute("select * from stu where mno=?",(m,))
        t=cur.fetchall()
        for i in t:
          print(i)
    if opt==4:
        b=input("enter the branch")
        cur.execute("select * from stu where branch=?",(b,))
        t=cur.fetchall()
        for i in t:
          print(i)
create_tb()
while 1:
 option=int(input("Enter the option\n1. insert\n2. see details of all students\n3. see details as per condition\n4. update\n5. delete in table \n6. drop table\n7. exit \n"))
 if option==1:
    insert_tb()
 elif option==2:
    display_tb()
 elif option==3:
    query_tb()
 elif option==4:
    update_tb()
 elif option==5:
    delete_tb()
 elif option==6:
    cur.execute("drop table stu")
    conn.commit()
 elif option==7:
     conn.close()
     exit()

