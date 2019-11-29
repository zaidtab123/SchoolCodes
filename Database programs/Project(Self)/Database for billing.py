import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="123456", database="db_zaid")
cursor = db.cursor()

try:
    i = 1
    while i > 0:
        cursor.execute("select SNo from product_details order by SNo desc limit 1")
        d= cursor.fetchone()
        i=int(d[0])
        s_no = i
        product = input('Enter the Product: ')
        price = float(input('Enter the price: '))
        value = str((s_no, product, price))
        print(value)
        insert_values = "insert into product_details values" + value
        cursor.execute(insert_values)
        db.commit()
        '''cursor.execute("select * from "+table_name)
        d = cursor.fetchall()
        print(d)'''
        x = input('Do you want to add more students[Y/N]: ')
        i+=1
        if x == 'n' or x == 'N':
            break
except:
    db.rollback()

db.close()
