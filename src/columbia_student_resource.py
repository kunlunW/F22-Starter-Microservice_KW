import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    # This is a static function that will connect to the database

    @staticmethod
    def _get_connection():

        usr = os.environ.get("DB_Username")
        pw = os.environ.get("DB_Password")
        h = os.environ.get("DB_Host")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        print("connecting successful!")
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

