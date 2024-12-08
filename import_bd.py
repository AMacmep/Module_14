import sqlite3

connections=sqlite3.connect('database.db')
cursor=connections.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Baza(
id INTEGER PRIMARY KEY,
product TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')
db_full = False
# cursor.execute( 'CREATE INDEX IF NOT EXISTS idx_email ON Baza (email)')
if not db_full:
    for n in range(1,5):
        cursor.execute('INSERT INTO Baza (product, description, price) VALUES (?, ?, ?)',
                       (f'Product_{n}', f'Низкокаллорийная полезная пища', n*100))
    db_full = True
connections.commit()
connections.close()

def select_info_from_db(number_product):
    connections = sqlite3.connect('database.db')
    cursor = connections.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Baza(
    id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    info_products=[]
    cursor.execute('SELECT product, description, price FROM Baza')
    products=cursor.fetchall()
    for product in products:
        info_products.append(f'Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}')
    connections.commit()
    connections.close()
    return info_products[number_product-1]
