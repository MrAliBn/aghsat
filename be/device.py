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
    CREATE TABLE IF NOT EXISTS device (
        id_device INT AUTO_INCREMENT PRIMARY KEY,
        code VARCHAR(220) NOT NULL,
        name VARCHAR(220) NOT NULL,
        phone VARCHAR(200)  NOT NULL,
        serial VARCHAR(200)  NOT NULL,
        price VARCHAR(200)  NOT NULL,
        model VARCHAR(200)  NOT NULL
    );
    """


cursor = connection.cursor()


class sabt_device:
    def __init__(self, code, name, phone, serial, price, model):
        self.code = code
        self.name = name
        self.phone = phone
        self.serial = serial
        self.price = price
        self.model = model


cursor.execute(create_users_table)
cursor.close()
