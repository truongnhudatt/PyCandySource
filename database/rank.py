import sqlite3

# con = sqlite3.connect('example.db')
# cur = con.cursor()
# # cur.execute('''CREATE TABLE tblUser
# #                 (name, scores)''')
# cur.execute('DELETE FROM tblUser')
# con.commit()
class Database:
    def __init__(self,databasename):
        self.con = sqlite3.connect(databasename)
        self.cur = self.con.cursor()

    def insert(self, name, scores):
        query = f"INSERT INTO tblUser VALUES('{name}','{scores}')"
        self.cur.execute(query)
        self.con.commit()

    def update(self, name, value):
        query = f"UPDATE tblUser SET scores = '{value}' WHERE name = '{name}'"
        self.cur.execute(query)
        self.con.commit()

    def select(self):
        query = "SELECT * FROM tblUser ORDER BY -scores"
        return self.cur.execute(query)


# data = Database(r"C:\Users\DatTanKy\PycharmProjects\PyCandy\example.db")
# data.
# # data.insert('Truong Nhu Dat', '100000')
# for row in data.select():
#     print(type(row))