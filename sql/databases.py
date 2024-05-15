import pymysql


class PymysqlClass:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset="utf8",
                port=self.port
            )
            print("Connected to the database!")
        except pymysql.Error as e:
            print(f"Error connecting to the database: {e}")

    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            print("Not connected to the database!")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed!")
        else:
            print("No connection to close!")

    def commit(self):
        if self.connection:
            self.connection.commit()
            print("Changes committed!")
        else:
            print("Not connected to the database!")

    def rollback(self):
        if self.connection:
            self.rollback()
            print('Rollback successfully')
        else:
            print('Rollback not successfully')




