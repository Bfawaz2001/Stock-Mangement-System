import sqlite3
from sqlite3 import Error

def create_table(con, create_sql_table):
    try:
        c = con.cursor()
        c.execute(create_sql_table)
        con.commit()
    except Error as e:
        print(e)
        
def StockMangementData():
    
    create_Brands_table = ''' CREATE TABLE IF NOT EXISTS "Brands" (
                                "BrandID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                "Brand_Name"	TEXT NOT NULL UNIQUE
                            );'''
    
    
    creat_Place_Order_table = '''CREATE TABLE IF NOT EXISTS "Place_Order" (
                                    "OrderID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                    "PIP"	INTEGER NOT NULL,
                                    "Order_Quantity"	INTEGER NOT NULL,
                                    "Total_Cost"	DECIMAL(6 , 2) NOT NULL,
                                    "Date_Placed"	DATETIME NOT NULL,
                                    FOREIGN KEY("PIP") REFERENCES "Product_Info"("PIP")
                                );'''
        
    create_Product_Info_table = ''' CREATE TABLE IF NOT EXISTS "Product_Info" (
                                        "PIP"	INTEGER NOT NULL UNIQUE,
                                        "BrandID"	INTEGER NOT NULL,
                                        "Product_Discription"	TEXT NOT NULL,
                                        "UseID"	INTEGER NOT NULL,
                                        "Pack_Size"	TEXT NOT NULL,
                                        "Product_Cost"	DECIMAL(6 , 2) NOT NULL,
                                        "SupplyID"	INTEGER NOT NULL,
                                        "Quantity"	INTEGER NOT NULL,
                                        PRIMARY KEY("PIP"),
                                        FOREIGN KEY("UseID") REFERENCES "Uses"("UseID"),
                                        FOREIGN KEY("SupplyID") REFERENCES "Supplier"("SupplyID"),
                                        FOREIGN KEY("BrandID") REFERENCES "Brands"("BrandID")
                                    );'''

    
    create_Supplier_table = ''' CREATE TABLE IF NOT EXISTS "Supplier" (
                                    "SupplyID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                    "Supply_Name"	TEXT NOT NULL UNIQUE,
                                    "Phone"	VARCHAR(11) NOT NULL UNIQUE,
                                    "Email"	TEXT NOT NULL UNIQUE,
                                    "Address"	TEXT NOT NULL UNIQUE
                                );'''
        
    create_Uses_table = ''' CREATE TABLE IF NOT EXISTS "Uses"(
                                "UseID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                "Use"	TEXT NOT NULL UNIQUE
                            );'''

    con = sqlite3.connect("Stock_Management_Database.db")

    if con is not None:
        create_table(con,create_Brands_table)

        create_table(con,creat_Place_Order_table)

        create_table(con,create_Product_Info_table)
        
        create_table(con,create_Supplier_table)
        
        create_table(con,create_Uses_table)

        con.close()
        
    else:
        print("Error! Can't create the Database Connection!")
    
StockMangementData()


            
