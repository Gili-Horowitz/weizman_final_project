import sqlite3
import os

# מחיקת בסיס נתונים קודם אם קיים
if os.path.exists("store.db"):
    os.remove("store.db")
    print("❌ Old database deleted.")
else:
    print("✅ No old database found.")


# יצירת טבלה ללקוחות (כולל עגלת קניות)
def create_tables():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # יצירת טבלת לקוחות עם עגלת קניות (שמות המוצרים בעגלה יהיו כטקסט מופרד בפסיקים)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        cart TEXT DEFAULT ''  -- שמות המוצרים בעגלה (מופרדים בפסיקים)
    )
    """)

    # יצירת טבלת מוצרים
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Tables created.")


# הוספת לקוח
def add_customer(name, phone):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()
    print(f"✅ Customer {name} added.")


# הוספת מוצר
def add_product(name, price):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()
    print(f"✅ Product {name} added.")


# הוספת מוצר לעגלת לקוח
def add_to_cart(customer_id, product_id):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # קבלת שם המוצר
    cursor.execute("SELECT name FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    if product is None:
        print("❌ Product not found.")
        conn.close()
        return

    product_name = product[0]

    # קבלת העגלה הנוכחית של הלקוח
    cursor.execute("SELECT cart FROM customers WHERE id = ?", (customer_id,))
    cart = cursor.fetchone()[0]

    # אם העגלה ריקה, אז פשוט נוסיף את שם המוצר
    if cart:
        new_cart = cart + "," + product_name
    else:
        new_cart = product_name

    # עדכון העגלה
    cursor.execute("UPDATE customers SET cart = ? WHERE id = ?", (new_cart, customer_id))

    conn.commit()
    conn.close()
    print(f"✅ Product {product_name} added to cart of customer {customer_id}.")


# תצוגת כל הלקוחות עם עגלת הקניות שלהם
def view_all_customers():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # קבלת כל הלקוחות
    cursor.execute("SELECT id, name, phone, cart FROM customers")
    customers = cursor.fetchall()

    if not customers:
        print("❌ No customers found.")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Cart':<30}")
        print("-" * 70)
        for customer in customers:
            print(f"{customer[0]:<5} {customer[1]:<20} {customer[2]:<15} {customer[3]:<30}")

    conn.close()


# תצוגת כל המוצרים
def view_all_products():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # קבלת כל המוצרים
    cursor.execute("SELECT id, name, price FROM products")
    products = cursor.fetchall()

    if not products:
        print("❌ No products found.")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Price':<10}")
        print("-" * 50)
        for product in products:
            print(f"{product[0]:<5} {product[1]:<20} ₪{product[2]:<10}")

    conn.close()


# דוגמה לשימוש
create_tables()  # יצירת טבלאות (פעם אחת בלבד)

# הוספת לקוחות
add_customer("Gili Horowitz", "053-4567890")
add_customer("Jane Smith", "058-6543210")
add_customer("David Levi", "054-9876543")
add_customer("Noa Azulai", "052-1239876")
add_customer("Eli Ben-David", "050-3456789")
add_customer("Dana Cohen", "054-0732701")
add_customer("Aviva Friedman", "053-9871234")
add_customer("Roni Avraham", "058-0735139")
add_customer("Daniella Harel", "054-5482943")


# הוספת מוצרים
add_product("Barbie", 55)
add_product("Lego", 60)
add_product("Plane", 25)
add_product("Bear", 35)
add_product("Car", 20)
add_product("Ball", 15)
add_product("Taki", 40)
add_product("Playmobli", 75)
add_product("ColoingBook", 15)
add_product("Light", 30)
add_product("Dinosaurs", 35)
add_product("CatDoll", 50)

# הוספת מוצרים לעגלות של לקוחות
add_to_cart(1, 1)  # הוספת מוצר עם מזהה 1 (Barbie) לעגלה של לקוח עם מזהה 1
add_to_cart(1, 2)  # הוספת מוצר עם מזהה 2 (Lego) לעגלה של לקוח עם מזהה 1
add_to_cart(2, 3)  # הוספת מוצר עם מזהה 3 (Plane) לעגלה של לקוח עם מזהה 2
add_to_cart(3, 12)
add_to_cart(3, 9)
add_to_cart(4, 5)
add_to_cart(5, 8)
add_to_cart(5, 10)
add_to_cart(5, 2)
add_to_cart(7, 7)
add_to_cart(7, 5)
add_to_cart(8, 3)
add_to_cart(8, 6)
add_to_cart(8, 7)
add_to_cart(8, 11)
add_to_cart(9, 9)

# הצגת הלקוחות עם העגלות שלהם
view_all_customers()

# הצגת כל המוצרים
view_all_products()

