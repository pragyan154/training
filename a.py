from flask import Flask
import mysql.connector
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fbfbaehfbhaekwfkjebfjk'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="activity"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE products999 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price FLOAT)")
# mycursor.execute("CREATE TABLE cart999 (id INT AUTO_INCREMENT PRIMARY KEY, product_id INT, quantity INT)")
# mycursor.execute("CREATE TABLE orders999 (id INT AUTO_INCREMENT PRIMARY KEY, product_id INT, quantity INT, customer_name VARCHAR(255))")

product_data = [
    ("Shirt", 20),
    ("Pants", 30),
    ("Dress", 39)
]

cart_data = [
    (1, 2),
    (2, 1)
]

order_data = [
    (1, 2, "rohan"),
    (2, 1, "goku")
]

insert_products = "INSERT INTO products999 (name, price) VALUES (%s, %s)"
mycursor.executemany(insert_products, product_data)

insert_cart = "INSERT INTO cart999 (product_id, quantity) VALUES (%s, %s)"
mycursor.executemany(insert_cart, cart_data)

insert_orders = "INSERT INTO orders999 (product_id, quantity, customer_name) VALUES (%s, %s, %s)"
mycursor.executemany(insert_orders, order_data)

@app.route('/')
def home():
    return "Welcome to the Cloth Store!"

@app.route('/products')
def products12():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM products999")
    products = cursor.fetchall()
    for p in products:
        print(p)
    return json.dumps(products)

@app.route('/cart')
def cart12():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM cart999")
    cart_items = cursor.fetchall()
    # for c in cart_items:
    #     print(c)
    return json.dumps(cart_items)

@app.route('/orders')
def orders12():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM orders999")
    orders = cursor.fetchall()
    # for o in orders:
    #     print(o)
    return json.dumps(orders)

if __name__ == '__main__':
    app.run(debug=True, port= 8080)