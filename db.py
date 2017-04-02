import MySQLdb


class Database:
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'janlinders'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, name, price, brand, weight, group):
        try:
            query = "INSERT INTO products (name, price, brand, weight, `group`) VALUES ('" + \
                    name + "', " + str(price) + ", '" + brand + "', '" + weight + "', '" + group + "')"
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def __del__(self):
        self.connection.close()
