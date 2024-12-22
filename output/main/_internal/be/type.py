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
print(f"Connected to database: {result}")


create_users_table = """
    CREATE TABLE IF NOT EXISTS type (
        id_type INT AUTO_INCREMENT PRIMARY KEY,
        code VARCHAR(220) NOT NULL,
        name VARCHAR(220) NOT NULL,
        phone VARCHAR(200)  NOT NULL,
        Type VARCHAR(200)  NOT NULL,
        tcname VARCHAR(200)  NOT NULL,
        g_m VARCHAR(200)  NOT NULL
    );
    """


cursor = connection.cursor()


class tala_chek:
    def __init__(self, code, name, phone, Type, tcname, g_m):
        self.code = code
        self.name = name
        self.phone = phone
        self.Type = Type
        self.tcname = tcname
        self.g_m = g_m


cursor.execute(create_users_table)
cursor.close()