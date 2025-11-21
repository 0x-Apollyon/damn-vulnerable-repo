import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT, balance REAL)")
cursor.execute("INSERT INTO accounts VALUES (1, 'JohnDoe', 1500.00)")
cursor.execute("INSERT INTO accounts VALUES (2, 'JaneSmith', 800.00)")
conn.commit()


def vulnerable_lookup(account_name):
    sql_query = f"SELECT * FROM accounts WHERE name = '{account_name}'"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result

print("Normal Result:", vulnerable_lookup("JohnDoe"))
