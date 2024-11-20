import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database='User',
    user='root',
    password='7804'
)

create_users_table = """
    CREATE TABLE IF NOT EXISTS aghsat (
        id_aghsat INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(220) NOT NULL,
        phone VARCHAR(200)  NOT NULL,
        price VARCHAR(200)  NOT NULL,
        time VARCHAR(200)  NOT NULL,
        status VARCHAR(200)  NOT NULL
    );
    """


cursor = connection.cursor()


class Sabt_Aghsat:
    def __init__(self, name, phone, price, time, status):
        self.name = name
        self.phone = phone
        self.price = price
        self.time = time
        self.status = status


cursor.execute(create_users_table)
cursor.close()

