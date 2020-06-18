import MySQLdb

class Dbconnect:

    def __init__(self,host,user,pwd,database):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.database = database

    def get_connection(self):
        self.conn = MySQLdb.connect(host = self.host,user=self.user,pwd=self.pwd,database=self.database)
        return self.conn

    

obj = Dbconnect("localhost","root","alpine","new")
obj.get_connection()

