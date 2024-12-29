import mysql.connector

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7804",
    database="user",
    auth_plugin="mysql_native_password"  # استفاده از پلاگین mysql_native_password
)

cursor = connection.cursor()
cursor.execute("SELECT DATABASE();")
result = cursor.fetchone()



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


