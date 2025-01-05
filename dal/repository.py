from be.User import connection
from be.aghsat import connection
from be.device import connection
from be.type import connection


class Repository:

    def execute_query(self, query, params=None, fetch=False):
        with connection.cursor() as cursor:
            cursor.execute(query, params or ())
            if fetch:
                return cursor.fetchall()
            connection.commit()
            return True
