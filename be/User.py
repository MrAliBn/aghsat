import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database='User',
    user='root',
    password='7804'
)


create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(220) NOT NULL,
        family VARCHAR(200)  NOT NULL,
        phone VARCHAR(200)  NOT NULL,
        date VARCHAR(200)  NOT NULL,
        time VARCHAR(200)  NOT NULL
    );
    """
cursor = connection.cursor()


class User:
    def __init__(self, name, family, phone, date, time):
        self.name = name
        self.family = family
        self.phone = phone
        self.date = date
        self.time = time


cursor.execute(create_users_table)
cursor.close()


