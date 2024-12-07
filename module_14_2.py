# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.

import sqlite3

connections = sqlite3.connect('not_telegram.db')
cursor = connections.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('DELETE FROM Users WHERE id=?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
total_number = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]

cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connections.commit()
connections.close()
