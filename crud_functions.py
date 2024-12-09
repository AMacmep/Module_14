import sqlite3


def initiate_db():
    connections = sqlite3.connect('products.db')
    cursor = connections.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    connections.commit()
    connections.close()


def fill_db():
    connections = sqlite3.connect('products.db')
    cursor = connections.cursor()

    for n in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт {n}', f'Низкокаллорийная полезная пища', n * 100))
    connections.commit()
    connections.close()


def get_all_products(id_product):
    connections = sqlite3.connect('products.db')
    cursor = connections.cursor()
    cursor.execute('SELECT * FROM Products WHERE id=?', (id_product,))
    check_product = cursor.fetchall()
    return check_product
    connections.close()
