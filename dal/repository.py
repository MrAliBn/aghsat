from be.User import connection
from be.aghsat import connection
from be.device import connection
from be.type import connection


class Repository:

    def adduser(self, data, obj):
        with connection.cursor() as cursor:
            sql_insert_query = f"""INSERT INTO {data} (name, family, phone, date, time) 
                                                  VALUES (%s, %s, %s, %s, %s)"""
            record_to_insert = (obj[0], obj[1], obj[2], obj[3], obj[4])
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()

    def addghest(self, data, obj):
        with connection.cursor() as cursor:
            sql_insert_query = f"""INSERT INTO {data} (code, name, phone, price, karmozd, koli, time, status, num) VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
            record_to_insert = (obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6], obj[7], obj[8])
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()

    def adddevice(self, data, obj):
        with connection.cursor() as cursor:
            sql_insert_query = f"""INSERT INTO {data} (code, name, phone, serial, price, model) VALUES 
            (%s, %s, %s, %s, %s, %s) """
            record_to_insert = (obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()

    def addtype(self, obj):
        print("ji")
        with connection.cursor() as cursor:
            sql_insert_query = """INSERT INTO type (code, name, phone, Type, tcname, g_m) VALUES 
            (%s, %s, %s, %s, %s, %s) """
            record_to_insert = (obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()

    def allusers(self, data):
        with connection.cursor() as cursor:
            sql_insert_query = f"""SELECT * FROM {data}"""
            cursor.execute(sql_insert_query)
            records = cursor.fetchall()
            return records

    def alluserswhere(self, data, status):
        with connection.cursor() as cursor:
            sql_insert_query = f"""SELECT * FROM {data} where status = %s"""
            cursor.execute(sql_insert_query, (status,))
            records = cursor.fetchall()
            return records

    def allusersday(self, data, date, status):
        with connection.cursor() as cursor:
            sql_insert_query = f"""SELECT * FROM {data} where time = %s AND status = %s"""
            cursor.execute(sql_insert_query, (date, status))
            records = cursor.fetchall()
            return records

    def allusersmonth(self, data, Year, Month, status):
        with connection.cursor() as cursor:
            sql_insert_query = f"""SELECT * FROM {data} WHERE SUBSTRING_INDEX(time, '/', 1) = %s  -- سال
                  AND SUBSTRING_INDEX(SUBSTRING_INDEX(time, '/', 2), '/', -1) = %s and status = %s"""
            cursor.execute(sql_insert_query, (Year, Month, status))
            records = cursor.fetchall()
            return records

    def allusersmonth2(self, data, Year, Month):
        with connection.cursor() as cursor:
            sql_insert_query = f"""SELECT * FROM {data} WHERE SUBSTRING_INDEX(time, '/', 1) = %s  -- سال
                  AND SUBSTRING_INDEX(SUBSTRING_INDEX(time, '/', 2), '/', -1) = %s"""
            cursor.execute(sql_insert_query, (Year, Month))
            records = cursor.fetchall()
            return records

    def Update(self, data, obj):
        with connection.cursor() as cursor:
            sql_insert_query = f"""UPDATE {data} set status = %s where id_aghsat = %s"""
            cursor.execute(sql_insert_query, (obj[0], obj[1]))
            connection.commit()
            cursor.close()
            return True

    def Exist(self, data, num):
        with connection.cursor() as cursor:
            sql_insert_query = f"""select * from {data} where phone = %s"""
            cursor.execute(sql_insert_query, (num,))
            records = cursor.fetchall()
            return records

    def Delete(self, data, code):
        with connection.cursor() as cursor:
            sql_insert_query = f"""DELETE FROM {data} WHERE code = %s"""
            cursor.execute(sql_insert_query, (code,))
            connection.commit()
            cursor.close()
            return True

    def CountUsers(self, data):
        with connection.cursor() as cursor:
            sql_insert_query = f"""SELECT COUNT(*) FROM {data}"""
            cursor.execute(sql_insert_query)
            records = cursor.fetchall()
            return records

    def CountUserWhere(self, data):
        with connection.cursor() as cursor:
            sql_insert_query = """SELECT COUNT(*) FROM aghsat where status = %s"""
            cursor.execute(sql_insert_query, (data,))
            records = cursor.fetchall()
            return records

    def CountUserWhere2(self, num, status):
        with connection.cursor() as cursor:
            sql_insert_query = """SELECT COUNT(*) FROM aghsat where phone = %s and status = %s"""
            cursor.execute(sql_insert_query, (num, status))
            records = cursor.fetchall()
            return records

    def searchdate(self, data, Year, Month):
        with connection.cursor() as cursor:
            query = f"""
                SELECT *
                FROM {data}
                WHERE SUBSTRING_INDEX(time, '/', 1) = %s  -- سال
                  AND SUBSTRING_INDEX(SUBSTRING_INDEX(time, '/', 2), '/', -1) = %s  -- ماه
                """
            cursor.execute(query, (Year, Month))
            records = cursor.fetchall()
            return records

    def CountaghsatMonth(self, Year, Month, status):
        with connection.cursor() as cursor:
            query = """SELECT COUNT(*) FROM aghsat WHERE SUBSTRING_INDEX(time, '/', 1) = %s  -- سال
                  AND SUBSTRING_INDEX(SUBSTRING_INDEX(time, '/', 2), '/', -1) = %s and status = %s"""
            cursor.execute(query, (Year, Month, status))
            records = cursor.fetchall()
            return records

    def CountaghsatMonth2(self, Year, Month):
        with connection.cursor() as cursor:
            query = """SELECT COUNT(*) FROM aghsat WHERE SUBSTRING_INDEX(time, '/', 1) = %s  -- سال
                  AND SUBSTRING_INDEX(SUBSTRING_INDEX(time, '/', 2), '/', -1) = %s"""
            cursor.execute(query, (Year, Month))
            records = cursor.fetchall()
            return records

    def CountaghsatWhere(self, time, status):
        with connection.cursor() as cursor:
            sql_insert_query = """SELECT COUNT(*) FROM aghsat where time = %s AND status = %s"""
            cursor.execute(sql_insert_query, (time, status))
            records = cursor.fetchall()
            return records

    def alldevice(self, data, phone, model):
        with connection.cursor() as cursor:
            sql_insert_query = f"""SELECT * FROM {data} where phone = %s and model = %s"""
            cursor.execute(sql_insert_query, (phone, model))
            records = cursor.fetchall()
            return records

    def Existaghsatcode(self, data, code):
        with connection.cursor() as cursor:
            sql_insert_query = f"""select * from {data} where code = %s"""
            cursor.execute(sql_insert_query, (code,))
            records = cursor.fetchall()
            return records

