from flask import Flask, render_template , request
import mysql.connector
import json

app = Flask(__name__, template_folder="/Users/prakhar.agnihotri/Documents/wiley_python/clone/training/templates")
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

# cart_data = [
#     (1, 2),
#     (2, 1)
# ]

# order_data = [
#     (1, 2, "rohan"),
#     (2, 1, "goku")
# ]

insert_products = "INSERT INTO products999 (name, price) VALUES (%s, %s)"
mycursor.executemany(insert_products, product_data)

# insert_cart = "INSERT INTO cart999 (product_id, quantity) VALUES (%s, %s)"
# mycursor.executemany(insert_cart, cart_data)

# insert_orders = "INSERT INTO orders999 (product_id, quantity, customer_name) VALUES (%s, %s, %s)"
# mycursor.executemany(insert_orders, order_data)

def insert_into_cart(product_id, quantity):
    mycursor = mydb.cursor()
    sql = "INSERT INTO cart999 (product_id, quantity) VALUES (%s, %s)"
    val = (product_id, quantity)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/products')
def products12():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM products999")
    products = cursor.fetchall()
    return render_template("products.html", products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    insert_into_cart(product_id, quantity)

    return "Product added to cart successfully!"

@app.route('/cart')
def cart12():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM cart999")
    cart_items = cursor.fetchall()
    return render_template("cart.html", cart_items=cart_items)

@app.route('/orders')
def orders12():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM orders999")
    orders = cursor.fetchall()
    return render_template("orders.html", orders=orders)

if __name__ == '__main__':
    app.run(debug=True, port=8080)