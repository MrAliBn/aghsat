from tkinter import messagebox

import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7804",
    database="user",
    auth_plugin="mysql_native_password"
)

cursor = connection.cursor()

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

try:

    with connection.cursor() as cursor:
        cursor.execute(create_users_table)
        connection.commit()
except Error as e:
    messagebox.showerror('error', f"Error while creating table: {e}")


class User:
    def __init__(self, name, family, phone, date, time):
        self.name = name
        self.family = family
        self.phone = phone
        self.date = date
        self.time = time


if __name__ == "__main__":
    cursor.close()
    connection.close()


