import sqlite3

class Database:
        def conn(slef):
            print("Database:connection method called")
            con=sqlite3.connect("mn.db")
            cur=con.cursor()
            query="create table if not exists product(pid integer primary key,pname text,price text,qty text,company text,contact text)"
            cur.execute(query)
            con.commit()
            con.close()
            print("Database:connection method finished\n")
       
        def insert(self,pid,pname,price,qty,company,contact):
            print("Database:insert method called")
            con=sqlite3.connect("mn.db")
            cur=con.cursor()
            query="insert into product values(?,?,?,?,?,?)"
            cur.execute(query,(pid,pname,price,qty,company,contact))
            con.commit()
            con.close()
            print("Database:insert method finished\n")
        def show(self):
            print("Database:show method called")
            con=sqlite3.connect("mn.db")
            cur=con.cursor()
            query="select*from product"
            cur.execute(query)
            rows=cur.fetchall()
            con.close()
            print("Database:show method finished\n")
            return rows
        def delete(self,pid):
            print("Database:delete method called",pid)
            con=sqlite3.connect("mn.db")
            cur=con.cursor()
            cur.execute("delete from product where pid=?",(pid,))
            con.commit()
            con.close()
            print(pid,"Database:delete method finished\n")
        def search(self,pid="",pname="",price="",qty="",company="",contact=""):
            print("Database:search method called",pid)
            con=sqlite3.connect("mn.db")
            cur=con.cursor()
            query="select*from product where pid=? or pname=? or price=? or qty=? or company=? or contact=?"
            cur.execute(query,(pid,pname,price,qty,company,contact))
            row=cur.fetchall()
            con.close()
            print(pid,"Database:search method finished\n")
            return row
        def update(pid,pname,price,qty,company,contact):
            print("Database:update method called",pid)
            con=sqlite3.connect("mn.db")
            cur=con.cursor()
            cur.execute("update product set pid=?, pname=? , price=? , qty=? , company=? , contact=? where pid=?",   (pid,pname,price,qty,company,contact,pid))
            con.commit()
            con.close()
            print(pid,"Database:update method finished\n")
   
