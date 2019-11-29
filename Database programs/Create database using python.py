import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="123456", database="db_zaid")
cursor = db.cursor()
table_name = input('Enter the name of the table: ')
cursor.execute('drop table if exists ' + table_name)
field_tuple = ' ('
a = 0
while a == 0:
    field_name = input('Enter the field name: ')
    field_datatype = input('Enter the datatype of the field: ')
    field_tuple += field_name + ' ' + field_datatype
    z = input('Do you want to add another field?[Y/N]: ')
    if z == 'n' or z == 'N':
        field_tuple += ');'
        break
    field_tuple += ','
create_table = "create table " + table_name + field_tuple
cursor.execute(create_table)

try:
    i = 1
    while i > 0:
        s_no = i
        product = int(input('Enter the class of student: '))
        price = int(input('Enter the age of student: '))
        value = str((s_no, product, price))
        insert_values = "insert into " + table_name + " values" + value
        cursor.execute(insert_values)
        db.commit()
        cursor.execute("select * from "+table_name)
        d = cursor.fetchall()
        print(d)
        x = input('Do you want to add more students[Y/N]: ')
        i+=1
        if x == 'n' or x == 'N':
            break
except:
    db.rollback()

db.close()
