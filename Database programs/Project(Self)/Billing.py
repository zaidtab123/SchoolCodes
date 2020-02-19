import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="123456", database="db_zaid")
cursor = db.cursor()

try:
    total=0
    bill=[]
    i=0
    while i>=0:
        buyingID=input("Enter the product ID:")
        quantity=int(input("Enter the quantity: "))
        exe_comm="select * from product_details where ProductID="+buyingID
        cursor.execute(exe_comm)
        x=cursor.fetchone()
        y=list(x)
        price=int(x[2])
        amount=price*quantity
        a=[quantity,amount]
        y.extend(a)
        bill.append(y)
        total+=amount
        continue_question=input("Would you like to continue[Y/N]: ")
        if continue_question == 'n' or continue_question == 'N':
            break

    l=len(bill)
    for i in range(l):
        print()
        for j in range(5):
            print(bill[i][j],end='       ')
        print()
    print("\nTotal value to be payed Rs.",total)
except:
    db.rollback()

db.close()