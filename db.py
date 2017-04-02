import MySQLdb


class Database:
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'janlinders'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

        stmt = "SHOW TABLES LIKE 'products'"
        self.cursor.execute(stmt)
        result = self.cursor.fetchone()
        if not result:
            # there are no tables named "tableName"
            sql = """CREATE TABLE `products` (
                              `name` varchar(100) NOT NULL,
                              `price` double NOT NULL,
                              `brand` varchar(45) NOT NULL,
                              `weight` varchar(45) NOT NULL,
                              `group` varchar(45) NOT NULL,
                              PRIMARY KEY (`name`,`price`,`brand`,`weight`)
                          ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
            self.cursor.execute(sql)

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
