import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    database='user',
    user='root',
    password='7804'
)


create_users_table = """
    CREATE TABLE IF NOT EXISTS aghsat (
        id_aghsat INT AUTO_INCREMENT PRIMARY KEY,
        code VARCHAR(220) NOT NULL,
        name VARCHAR(220) NOT NULL,
        phone VARCHAR(200)  NOT NULL,
        price VARCHAR(200)  NOT NULL,
        karmozd VARCHAR(200)  NOT NULL,
        koli VARCHAR(200)  NOT NULL,
        time VARCHAR(200)  NOT NULL,
        status VARCHAR(200)  NOT NULL,
        num VARCHAR(200)  NOT NULL
    );
    """


cursor = connection.cursor()


class Sabt_Aghsat:
    def __init__(self, code, name, phone, price, karmozd, koli, time, status, num):
        self.code = code
        self.name = name
        self.phone = phone
        self.price = price
        self.karmozd = karmozd
        self.koli = koli
        self.time = time
        self.status = status
        self.num = num


cursor.execute(create_users_table)
cursor.close()

