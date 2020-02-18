import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="123456", database="db_zaid")
cursor = db.cursor()

try:
    i = 1
    while i > 0:
        cursor.execute("select max(SNo) from product_details")
        d= cursor.fetchone()
        if d[0] == None:
            s_no = 1
        else:
            s_no = d[0]+1
        product = input('Enter the Product: ')
        price = float(input('Enter the price: '))
        value = str((s_no, product, price))
        print(value)
        insert_values = "insert into product_details values" + value
        cursor.execute(insert_values)
        db.commit()
        cursor.execute("select * from product_details")
        d = cursor.fetchall()
        print(d)
        x = input('Do you want to add more products[Y/N]: ')
        i+=1
        if x == 'n' or x == 'N':
            break
except:
    db.rollback()

db.close()
