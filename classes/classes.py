# # Bank Account:
# Create a class called "BankAccount" that represents a 
# bank account. It should have attributes such as the account number, 
# account holder name, and balance. Implement methods to deposit and 
# withdraw money from the account, and a method to display the current balance.

class Bankaccount:
    def __init__(self,accountnumber,accountname,balance):
        self.accountnumber=accountnumber
        self.accountname=accountname
        self.balance=balance
    def Balance(self):
        return f"your current balance is {self.balance}"     

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        return f"withdrawal of {amount} successful your balance is {self.balance}"      
    
    
     
account1=Bankaccount(123456,"Rita khaseyi",50000)
print(account1.withdraw(5000))
print(account1.withdraw(5000))
print(account1.Balance())     


    

# Student Record:
# Create a class called "Student" that represents a student's record. 
# It should have attributes such as the student's name, roll number, 
# and a dictionary to store the subject-wise marks. Implement methods
#  to add marks for different subjects, calculate the total marks,
#  and display the student's record.
class Student:
    def __init__(self,studentname,codenumber):
        self.studentname=studentname
        self.codenumber=codenumber
        self.marks={}
    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def calculate_total_marks(self):
        total_marks = sum(self.marks.values())
        return total_marks

    def display_record(self):
        print("Student Record:")
        print("Name:", self.studentname)
        print("Roll Number:", self.codenumber)
        print("Marks:")
        for subject, marks in self.marks.items():
            print(f"{subject}: {marks}")
        total_marks = self.calculate_total_marks()
        print("Total Marks:", total_marks)    
# Creating an instance of Student
student = Student("John Doe", "12345")

# Adding marks for different subjects
student.add_marks("Math", 90)
student.add_marks("Science", 85)
student.add_marks("English", 92)

# Displaying the student's record
student.display_record()


# Car:
# Create a class called "Car" that represents a car. 
# It should have attributes such as the make, model, year, 
# and color. Implement methods to start the car, stop the 
# car, and display its details.
class Car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    def start(self):
        print(f"the {self.color} {self.make} {self.model} is being driven")  
    def stop(self):
        print(f"the {self.color} {self.make},{self.model} has stopped")  
    def details(self):
        print(f"this is a {self.color} {self.make} {self.model} {self.year} car")        
car = Car("Toyota", "Camry", 2022, "Silver")
car.stop()
car.start()
car.details()        
# Library Book:
# Create a class called "Book" that represents a library book. 
# It should have attributes such as the book title, author name, 
# and availability status. Implement methods to check out the book, 
# return the book, and display the book's details.

class Book:
    def __init__(self,title,author,availability):
        self.title=title
        self.author=author
        self.availability=availability
    def checkout(self):
        if self.availability:
            self.availability=False
            print(f"The book '{self.title}' by {self.author} has been checked out.")   
        else:
            print(f"Sorry, the book '{self.title}' by {self.author} is currently unavailable.")
    def returnbook(self):
        if not self.availability:
            self.availability = True
            print(f"The book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"The book '{self.title}' by {self.author}' was not checked out.")
    def details(self):
        
        status = "Available" if self.availability else "Not available"
        print(f"the book {self.title} by {self.author} is {status}")
book = Book("The Great Gatsby", "F. Scott Fitzgerald",False) 
book1=Book("Born a crime","trevor noah",True)
book.checkout()
book.returnbook()
book.details() 
book1.checkout()
book1.returnbook()
book1.details()   
       

        

          


     

# Rectangle:
# Create a class called "Rectangle" that represents a rectangle.
#  It should have attributes such as the length and width. Implement 
# methods to calculate the area and perimeter of the rectangle, and a 
# method to display its dimensions.

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        area=self.width*self.length
        print(f"the area is {area}")
    def perimeter(self):
        perimeter=(self.width+self.length)*2
        print(f"the perimeter is {perimeter}")
    def dimensions(self):
        print(f"the rectangle has a length of {self.length} and a width of {self.width}") 
rectangle1=Rectangle(4,5)
rectanle2=Rectangle(6,5) 
rectangle1.area()
rectanle2.area()
rectangle1.perimeter()
rectanle2.perimeter()
rectangle1.dimensions()
rectanle2.dimensions()


# Create a class called Rectangle with attributes width and height. 
# Implement a method called area() that calculates and returns the area of the rectangle.
class Rectangles:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        are=self.width * self.height
        print(f"the area of the rectangle is {are}")
rect1=Rectangles(4,5) 
rect1.area()  




# Create a class called Person with attributes name and age.
#  Implement a method called greet() that prints a greeting
#  message including the person's name.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hello my name is {self.name} and i am {self.age}") 
person1=Person("rita khaseyi",22)  
person1.greet()         
        

# Create a class called BankAccount with attributes 
# account_number and balance. Implement methods deposit()
#  and withdraw() that modify the balance accordingly.


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Balance is {self.balance}.")
        else:
            print("Insufficient balance for withdrawal.")

account = BankAccount(23566, 500)
account.deposit(1000)
account.withdraw(500)

        

        

# Create a class called Circle with attribute radius.
#  Implement methods area() and circumference() that calculate and 
# return the area and circumference of the circle, respectively.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        areas= 3.14*self.radius*self.radius
        return f"the area of the circle is {areas}" 
    def circumference(self):
        circ=(3.14*self.radius)*2  
        return f"the circumference is {circ}"
circle1=Circle(5)
print(circle1.area())
print(circle1.circumference())    

        

# Create a class called Car with attributes make, model, and year.
#  Implement a method called start() that prints a message indicating 
# that the car has started.
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print(f"the {self.make} {self.model} {self.year} car is being driven")  
car1=Car("bhughatti","Bolide",2021) 
car1.start()         

# Create a class called Student with attributes name, grade, and scores.
#  Implement a method called average_score() that calculates and returns
#  the average score of the student.
class Student:
    def __init__(self,name,grade,scores):
        self.name=name
        self.grade=grade
        self.scores=scores
    def average_score(self):
        
        total = sum(self.scores)
        average = total / len(self.scores)
        print(f"The average score is {average:.2f}")
            

        
         
student1=Student("rita",'A',[80,80,80,80,80]) 
student1.average_score()  

            



# Create a class called Bank with an attribute name and a list attribute accounts.
#  Implement a method called add_account() that adds a new account to the list.
class Bank:
    def __init__(self,name,accounts):
        self.name=name
        self.accounts=accounts
    def add_acount(self,account):
        self.accounts.append(account) 
        print(self.accounts)  
bank1=Bank("kcb",[23,45,67,78])
bank1.add_acount(34)         


# Create a class called Dog with attributes name and age.
#  Implement a method called bark() that prints a message with 
# the dog's name and "barks".
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"the {self.age} year old {self.name} barks")  

dog1=Dog("german shepherd",1)
dog1.bark()
# Create a class called Email with attributes sender,
#  recipients, and message. Implement a method called send()
#  that prints a message indicating that the email has been sent.
class Email:
    def __init__(self,sender,recipients,message):
        self.sender=sender
        self.recipients=recipients
        self.message=message
    def send(self):
        print(f"the {self.message} message from {self.sender} has been succesfully sent to {self.recipients}")
email1=Email("kenyani","rita","buy a book first")  
email1.send()          

# Create a class called Book with attributes 
# title, author, and year. Implement a method called get_info()
#  that returns a string with the book's information.
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def get_info(self):
        return f"the book {self.title} by {self.author} was published in the year {self.year}"
book1=Book("born a crime","trevor noah",2010)  
print(book1.get_info())  