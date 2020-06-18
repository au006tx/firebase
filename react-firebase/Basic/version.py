import sys
import MySQLdb as m

class Version:

    def __init__(self,host,user,pwd,database):
        self.host = host
        self.user = user
        self.pwd  = pwd
        self.database = database


    def get_version(self):
        
        con = m.connect(self.host,self.user,self.pwd,self.database)
        cur = con.cursor()
        cur.execute("select version()")
        data = cur.fetchall()
        print "Database version:{}".format(data)

    def create_table(self):
        
        try:
            con = m.connect(self.host,self.user,self.pwd,self.database)
            cur = con.cursor()
            create = "create table Movie(id int PRIMARY KEY,MovieName varchar(32),Actor varchar(32))"
            cur.execute(create)
            cur.fetchall()

        except Exception as e:
            print("Exception occured: {}".format(e))
            
        finally:

            cur.execute("show tables")
            row = cur.fetchall()
            print(row)

    
        

obj = Version("localhost","root","alpine1234","new")
obj.get_version()
obj.create_table()



