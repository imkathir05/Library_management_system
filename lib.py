import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="library2"
)

cursor = db.cursor()

print("1. Signup")
print("2. Login")

choice = int(input("Enter your choice: "))

if choice == 1:
    id = int(input("Enter id: "))
    Name = input("Enter the Name: ")
    Email = input("Enter the Email: ")
    Mobile_No = int(input("Enter the Mobile_No: "))

    query = "INSERT INTO borrowers (id, Name, Email, Mobile_No) VALUES (%s, %s, %s, %s)"
    values = (id, Name, Email, Mobile_No)

    cursor.execute(query, values)
    db.commit()
    print("Signup successfully")

elif choice == 2:
    Email = input("Enter the Email: ")
    Mobile_No = int(input("Enter the Mobile_No: "))

    query = "SELECT * FROM borrowers WHERE Email = %s AND Mobile_No = %s"
    values = (Email, Mobile_No)

    cursor.execute(query, values)

    result = cursor.fetchall()

    if result:
        print("Login successfully")
    else:
        print("Login failed. Please check your Email and Mobile_No.")


print("options:")
l=["1.Addbook","2.viewbook","3.Borrowerdetails","4.Borrow","5.Return"]
for i in l:
    print(i)
choice=input("Enter your choice:")

if choice==1: #choice1 is for Add book in a Library
    id=int(input("Enter the id:"))
    Author=input("Enter the Author Name:")
    Title=input("Enter the Title:")
    query="insert into books (id,Author,Title)values(%s,%s,%s)"
    values=(id,Author,Title)
    cursor.execute(query,values)
    db.commit()
    print("Book Added Successfully")
    
elif(choice==2):#choice2 is for view all books
    query="select * from books"
    cursor.execute(query)
    result=cursor.fetchall()
    print("\nBooks in the Library:")
    for book in result:
        print(book)
        
        
elif(choice==3):#view borrower details
    query="select * from borrower"
    cursor.execute(query)
    result=cursor.fetchall()
    db.commit()
    print("Borrower details:")
    for i in result:
        print(i)    
    
elif(choice==4):#choice4 is for the borrowing the books
    Title=input("Enter the Title Name:")
    Author=input("Enter the Author Name: ")
    query="delete from books where Title=%s and Author=%s"
    values=(Title,Author)
    cursor.execute(query,values)
    db.commit()
    print("Book Borrowed Successfully")
elif(choice==5):#choice5 is for Returning the Borrowed books
    id=int(input("Enter the id book id:"))
    Title=input("Enter the Title Name:")
    Author=input("Enter the Author Name: ")
    query="insert into books (id,Author,Title)values(%s,%s,%s) "
    values=(id,Title,Author)
    cursor.execute(query,values)
    db.commit()
    print("Book Returned Successfully")

db.close()

