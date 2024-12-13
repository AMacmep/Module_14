import sqlite3

# Создание баз данных products.db и users.db
def initiate_db():
    connections = sqlite3.connect('products.db')
    cursor = connections.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connections.commit()
    connections.close()

    connections = sqlite3.connect('users.db')
    cursor = connections.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')
    connections.commit()
    connections.close()


# Заполнение базы данных users, внесение дополнительных данных
def add_user(username, email, age):
    connections = sqlite3.connect('users.db')
    cursor = connections.cursor()
    if is_included(username):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connections.commit()


def is_included(username_incl):
    connections = sqlite3.connect('users.db')
    cursor = connections.cursor()
    print(cursor.execute('SELECT * FROM Users WHERE id=?', (username_incl,)))
    return cursor.execute('SELECT * FROM Users WHERE id=?', (username_incl,))=='None'
    connections.commit()
    connections.close()


# Заполнение баз данных
def fill_db():
    connections = sqlite3.connect('products.db')
    cursor = connections.cursor()

    for n in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт {n}', f'Низкокаллорийная полезная пища', n * 100))
    connections.commit()
    connections.close()


# Извлечение данных из баз данных
def get_all_products(id_product):
    connections = sqlite3.connect('products.db')
    cursor = connections.cursor()
    cursor.execute('SELECT * FROM Products WHERE id=?', (id_product,))
    check_product = cursor.fetchall()
    return check_product
    connections.commit()
    connections.close()


initiate_db()
add_user('Ivan', 'iv@mail.ru', 35)
add_user('Fedor', 'fe@mail.ru', 38)
add_user('Andrey', 'an@mail.ru', 42)
add_user('Andrey', 'an2@mail.ru', 15)