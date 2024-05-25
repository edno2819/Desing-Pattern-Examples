class DatabaseConnection:
    _instance = None
    count = 0

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
        cls.count += 1
        return cls._instance

    def connect(self):
        print(self.count)


a = DatabaseConnection()
a.connect()
b = DatabaseConnection()
b.connect()
c = DatabaseConnection()
c.connect()


