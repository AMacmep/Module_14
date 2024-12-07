# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."
# Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.

import sqlite3

connections=sqlite3.connect('not_telegram.db')
cursor=connections.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute( 'CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for n in range(1,11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{n}', f'example{n}@gmail.com', n*10,  1000))
for n1 in range(1,11,2):
    cursor.execute('UPDATE Users SET balance=? WHERE username =?', (500,f'User{n1}'))

for n2 in range(1,11,3):
    cursor.execute('DELETE FROM Users WHERE username=?', (f'User{n2}',))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <>?',(60,))
users=cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]},| Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connections.commit()
connections.close()