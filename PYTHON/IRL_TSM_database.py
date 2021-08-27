import sqlite3

tables = ("products", "receipts", "purchases")
databasePath = r'..\Databases\IRL_TSM.db'

def customCommand(command):
    database = sqlite3.connect(databasePath)
    c = database.cursor()
    c.execute(command)
    database.commit()
    database.close()

def createDatabase():
    database = sqlite3.connect(databasePath)
    c = database.cursor()
    c.execute("""CREATE TABLE products(
        name text,
        kaufland_id text,
        auchan_id text,
        biedronka_id text,
        carrefour_id text,
        tags text,
        value real,
        unit text,
        energy real,
        fat real,
        saturated_fat real,
        trans_fat real,
        salt real,
        carbohydrate real,
        fiber real,
        sugar real,
        protein real,
        calcium real,
        chromium real,
        copper real,
        flouride real,
        iodine real,
        iron real,
        magnesium real,
        manganese real,
        molybdenum real,
        phosphorus real,
        selenium real,
        zinc real
    )
    """)
    database.commit()
    database.close()

def addProduct(name, id, kaufland_id = None, auchan_id = None, biedronka_id = None, carrefour_id = None, \
    tags = None, value = None, unit = None, energy = None, fat = None, saturated_fat = None, \
    trans_fat = None, salt = None, carbohydrate = None, fiber = None, sugar = None, protein = None, \
    calcium = None, chromium = None, copper = None, flouride = None, iodine = None, iron = None, \
    magnesium = None, manganese = None, malybdenum = None, phosphorus = None, selenium = None, zinc = None):

    database = sqlite3.connect(databasePath)
    c = database.cursor()
    c.execute("""INSERT INTO products VALUES 
    (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (name, kaufland_id, auchan_id, biedronka_id, carrefour_id, tags, value, unit, energy, fat,\
    saturated_fat, trans_fat, salt, carbohydrate, fiber, sugar, protein, calcium, chromium, copper,\
    flouride, iodine, iron, magnesium, manganese, malybdenum, phosphorus, selenium, zinc, id))
    database.commit()
    database.close()

#return added receipt's rowid
def addReceipt(date, shop = None, image = None):
    #TODO write me!
    return True

def addPurchase(product_id, receipt_id, amount_bought, unit):
    #TODO write me!
    return True

def deleteEntry(rowid):
    database = sqlite3.connect(databasePath)
    c = database.cursor()
    rowid = str(rowid)
    c.execute("SELECT * FROM products WHERE rowid = ?", (rowid))
    print("To permanently delete this record type 'y':")
    print(c.fetchall())
    userInput = input()
    if userInput == 'y':
        c.execute("DELETE FROM products WHERE rowid = ?", (rowid))
    database.commit()
    database.close()


def printAll(table):
    database = sqlite3.connect(databasePath)
    c = database.cursor()
    c.execute("SELECT rowid,* FROM ?", (table))
    rows = c.fetchall()
    for row in rows:
        print(row)
    database.commit()
    database.close()


if __name__ == "__main__":
    for table in tables:
        printAll(table)
        print()
    print("Exit success")