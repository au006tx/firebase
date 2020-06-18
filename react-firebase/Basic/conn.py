import MySQLdb
class DBConnection:
    def __init__(self, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME):
        self.host = DB_HOST
        self.name = DB_NAME
        self.user = DB_USER
        self.password = DB_PASSWORD
        

    def get_conn(self):
        self.conn = MySQLdb.connect(host = self.host,
                                    db = self.name,
                                    user = self.user,
                                    passwd = self.password)
        return self.conn

obj = DBConnection("localhost","root","alpine","new")
obj.get_conn()