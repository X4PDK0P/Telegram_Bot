import sqlite3
import time

db = sqlite3.connect('db.db')
cursor = db.cursor()

# delete table users
#cursor.execute('DROP TABLE users')

cursor.execute('''CREATE TABLE  IF NOT EXISTS users(
            user_id BIGINT,
            subscription_validity_period INTEGER, 
            svp_for_code INTEGER)
            ''')
# Maybe save the changes
db.commit()

input_user_id = int(input('USER_ID: '))
input_subscription_validity_period = int(input('subscription_validity_period: '))


def add_new_line():
    cursor.execute('SELECT user_id FROM users')
    # add info in datebase
    cursor.execute(f'INSERT INTO users VALUES (?, ?, ?)', (input_user_id,
                                                           input_subscription_validity_period,
                                                           input_subscription_validity_period))
    db.commit()


add_new_line()


def delete_user_from_db():
    cursor.execute('DELETE FROM users WHERE subscription_validity_period == 0')


if time == 0:
    delete_user_from_db()


def search_info():
    cursor.execute('SELECT * FROM users')

    all_results = cursor.fetchall()
    print('People with subscription:', all_results)


search_info()


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

if (int(time.time()) - last_update) > 86400:
    change_svp()
    last_update = int(time.time())

db.close()
