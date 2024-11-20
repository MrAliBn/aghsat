from be.User import connection
from be.aghsat import connection

cursor = connection.cursor()


class Repository:

    def adduser(self, data, obj):
        sql_insert_query = f"""INSERT INTO {data} (name, family, phone, date, time) 
                                              VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (obj[0], obj[1], obj[2], obj[3], obj[4])
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()

    def addghest(self, data, obj):
        sql_insert_query = f"""INSERT INTO {data} (name, phone, price, time, status) VALUES (%s, %s, %s, %s, %s) """
        record_to_insert = (obj[0], obj[1], obj[2], obj[3], obj[4])
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()

    def allusers(self):
        sql_insert_query = """SELECT * FROM users"""
        cursor.execute(sql_insert_query)
        records = cursor.fetchall()
        return records

    def Exist(self, data, num):
        sql_insert_query = f"""select * from {data} where phone = %s"""
        cursor.execute(sql_insert_query, (num,))
        records = cursor.fetchall()
        return records

