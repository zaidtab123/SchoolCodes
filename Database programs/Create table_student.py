import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="123456", database="db_zaid")
cursor = db.cursor()
cursor.execute('drop table if exists student')
create_table = """create table student(name varchar(20), class int, age int);"""
cursor.execute(create_table)
try:
    i = 0
    while i == 0:
        name = input('Enter the name of student: ')
        stud_class = int(input('Enter the class of student: '))
        stud_age = int(input('Enter the age of student: '))
        value = (name, stud_class, stud_age)
        insert_values = """insert into student(name,class,age) values(%s,%s,%s)"""
        cursor.execute(insert_values, value)
        db.commit()
        cursor.execute("""select * from student""")
        d=cursor.fetchall()
        print(d)
        x = input('Do you want to add more students[Y/N]: ')
        if x == 'n' or x == 'N':
            break
except:
    db.rollback()

db.close()
