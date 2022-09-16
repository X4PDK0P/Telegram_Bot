import sqlite3
import time

db = sqlite3.connect('db.db')
cursor = db.cursor()

while True:

    def change_svp():
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for i in rows:
            sql_update_query = """UPDATE users SET subscription_validity_period = (svp_for_code - 1)"""
            cursor.execute(sql_update_query)
            db.commit()

        for i in rows:
            sql_update_query_1 = """UPDATE users SET svp_for_code = (subscription_validity_period)"""
            cursor.execute(sql_update_query_1)
            db.commit()


    last_update = int(time.time())

    if (int(time.time()) - last_update) > 60:
        change_svp()
        last_update = int(time.time())
#86400

