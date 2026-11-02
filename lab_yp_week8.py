import sqlite3

def create_table():
    conn = sqlite3.connect("bank.bd")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts(id INTEGER PRIMARY KEY, name TEXT, balance REAL)")
    conn.commit()
    conn.close()

def insert_info():
    conn = sqlite3.connect("bank.bd")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts(name, balance) VALUES('Kolya', 1500)")
    cursor.execute("INSERT INTO accounts(name, balance) VALUES('Petya', 2500)")
    conn.commit()
    conn.close()

def delete_info(a):
    conn = sqlite3.connect("univercity.bd")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", a)
    conn.commit()
    conn.close()


#create_table()

#insert_info()

for a in range(10):
    delete_info(a)
   
try:
    conn = sqlite3.connect("bank.bd")
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = balance - 1000 WHERE id = 1")
    raise Exception("Power Failure")
    cursor.execute("UPDATE accounts SET balance = balance + 1000 WHERE id = 2")
    conn.commit()
except:
    conn.rollback()
conn.close()

