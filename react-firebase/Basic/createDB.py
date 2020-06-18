import MySQLdb as mysql


class Movie:

    def __init__(self,host,user,pwd):

        self.host = host
        self.user = user
        self.pwd = pwd

    def create_database(self):

        """ Creates the New Database in Mysql Server"""
        
        try:
            conn = mysql.connect(self.host,self.user,self.pwd)
            cur  = conn.cursor()
            create = "create database new_salman"
            cur.execute(create)
            cur.fetchall()

        except Exception as e:
            print("Exception occured {}".format(e))

        finally:

            show = "show databases"
            cur.execute(show)
            data = cur.fetchall()
            print(data)
    

    def __init__(self,host,user,pwd,database):

            self.host = host
            self.user = user
            self.pwd = pwd
            self.database = database

    def create_table_Movie(self):

        try:

            con = mysql.connect(self.host,self.user,self.pwd,self.database)
            cur = con.cursor()
            create = "create table Movie(id int PRIMARY KEY,MovieName varchar(32),Actor varchar(32))"
            cur.execute(create)
            cur.fetchall()

        except Exception as e:
            print("exception occured {}".format(e))

        finally:
            cur.execute("show tables")
            row = cur.fetchall()
            print(row)

    def insert_into_Movie_Table(self):



        value = [('001','spiderman','spider')]
        query = "insert into Movie(id,Moviename,Actor) values(%s,%s,%s)"

        con = mysql.connect(self.host,self.user,self.pwd,self.database)
        cur = con.cursor()
        cur.execute(query,value)
        val = cur.fetchall()
        print(val)




    


obj1 = Movie("localhost","root","alpine1234","new_salman")
obj1.create_database()
obj1.create_table_Movie()
obj1.insert_into_Movie_Table()
