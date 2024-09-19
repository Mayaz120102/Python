# thislist =["apple","banana","cherry"]
# print(thislist)
# thislist =["pple","banana","cherry"]
# thislist.sort()
# print(thislist)
# # print(thislist[0])
# # thislist[2]= "lichu"
# # print(thislist[2])
# # print(thislist)
# # newlist =["am","jam","kathal"]
# # print(newlist)
# # thislist.extend(newlist)
# # print(thislist)
# # thislist.remove("apple")
# # print(thislist)

# marks = int(input("Enter your marks: "))

# if(marks>=90):
#     print("A")
# elif(marks<90 and marks>=80):
#     print("B")
# elif(marks<80 and marks>=70):
#     print("C")
# else:
#     print("D")

# if(marks%2==0):
#     print("even")
# else:
#     print("odd")

# a,b,c = map(int,input("enter three numbers: ").split())
# print(a,b,c)

# if(a>=b and a>=c):
#     print("a")
# elif(b>=c):
#     print("b")
# else:
#     print("c")
# m [] 
# print("input three of your fav movies name: ")
# m1  = input()
# m2  = input()
# m3  = input()

# print(m1,m2,m3)

# m.append(m1)
# m.append(m2)
# m.append(m3)

# print(m)
# print(type(m))

#----------------- 0 -----------------#

# Dictionary in python

# info ={
#     "key" : "value",
#     "name": "mayaz",
#     "age" : 24,
#     "dept" :{
#         "cse" : 5,
#         "eee" : 4,
#         "civil" : 2
#     }
# }

# print(info)
# print(info["dept"])

# print(info.keys())

#----------------- 0 -----------------#


#Sets in python

# collection ={1,2,3,5,4}
# print(collection)

# collection =set()
# print(type(collection))

#----------------- 0 -----------------#

# loops

# n = int(input("enter the number: "))
# i =1
# while i<=10:
#     print(i*i)
#     # print("mayaz")
#     i+=1

# list = [1,4,9,16,25,36,49,64,81,100]

# i=0
# while i<len(list):
#     print(list[i])
#     i+=1

# tuple = (1,4,9,16,25,36,49,64,81,100)

# x= 36 
# i =0
# while i<len(tuple):
#   if(tuple[i]==x):
#     print("found at",i)
#   i+=1

# n = int(input("enter the number: "))
# i =1
# sum =0

# while i<=n:
#   sum+=i
#   i+=1

# print(sum)

# n = int(input("enter the number: "))

# fact =1
# i =1

# # while i<=n:
# #   fact*=i
# #   i+=1
# # print(fact)

# for i in range(1,n+1):
#   fact*=i

# print(fact)

# =================================000==========================#

#function in python 
# def sum(a,b):
#   s= a+b
#   print(s)
#   return s

# sum(1,2)
# sum(12,25)

# sum(45,24)

# sum(5,2)

# def avg(a,b,c):
#   avg= (a+b+c)/3
#   print(avg)
#   return avg

# avg(1,2,3)

# food = ["burger" , "pizza", "sandwitch"]
# drinks = ["pepsi", "mojo", "starship"]

# def list_len(list):
#   print(len(list))

# list_len(food)
# list_len(drinks)

# def list_val(list):
#   for val in list:
#     print(val, end =" ")

# list_val(food)
# print("\n")
# list_val(drinks)

# def factorial(n):
#   fact =1
#   for val in range(1,n+1):
#     fact*=val
#   print(fact)

# factorial(4)   

# def conv(usd_val):
#   print(usd_val*119.54)

# conv(5)
# conv(1000)

# ======================= 0 ======================

#Recursion in python 

# def display(n):
#   if(n == 0):
#     return 
#   print(n)
#   display(n-1)

# display(5)

# def n_factorial(n):
#   if(n == 0 or n==1):
#     return 1
#   else:
#     return n_factorial(n-1)*n

# print(n_factorial(5)) 

  
#q1

# def n_sum(n):
#   if(n==0):
#     return 0
#   else:
#     return n_sum(n-1)+n
# print(n_sum(5))

# q2

# f= open("python.txt","r")

# data = f.read()
# print(data)
# f.close()

# line1= f.readline()
# print(line1)

# line2 =f.readline()
# print(line2)

# line3 =f.readline()
# print(line3)

# f = open("python.txt","a+")
# print(f.read())
# f.write("hola amigos assa")


# f.close()

# import os  
# os.remove("python.txt")
# f= open("python.txt", "a")
# f.close()

# with open("practice.txt","r") as f:
#     data =f.read()
#     if(data.find("python")!=-1):
#         print("found")
#     else:
#         print("not found")   

# def linecheclk():
#     data = True
#     linno =1
#     with open("practice.txt","r") as f:
#         while data:
#             data= f.readline()
#             if("learningg" in data):
#                 print(linno)
#                 return
#             linno+=1

#     return -1           
# linecheclk()       

# ============0=====================

# OOP in python:

# class Student:
#     clg_name = "city college"
# ---------contructor:
#     def __init__(self,name,marks):
#         self.name = name     
#         self.marks = marks
# ------methods:
#     def omma(self):
#         print("omma kire", self.name,self.marks)
# -----object---
# s1 = Student("mayaz",97)
# s1.omma()

# q1 
# class Student:
#  # contructor----------
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks= marks

#  #---methods
#     def show(self):
#         print(self.name,",",self.marks)

#     def calc_avg(self):
#         sum =0
#         for val in self.marks:
#             sum+=val
#         print("avg is: ",sum/3)

# # object and calls
# s1 = Student("mayaz",[100,50.78])
# s1.show()
# s1.calc_avg()

# abstraction:
# class Car:
#     # contructor
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     # methods
#     def start(self):
#         self.start = True
#         self.clutch = True
#         print("car started")

# step = Car()
# step.start()


# q2 
# class Account:
#     def __init__(self,balance,acno):
#         self.balance = balance
#         self.acno = acno
    
#     def debit(self,amount):
#         self.balance -= amount
#         print("amount" ,amount,"was debited")
#         print("tot bal",self.fin_bal())

#     def credit(self,amount):
#         self.balance += amount
#         print("amount ",amount ,"was credited")
#         print("tot bal",self.fin_bal())

#     def fin_bal(self):
#         return self.balance

# acno1 = Account(10000,4521)
# acno1.debit(100)
# acno1.credit(20)
# acno1.credit(1)
# # print(acno1.balance)
# # print(acno1.acno)
  
# Private and public:
# private:

# class Person:
#     __name = "mayaz"

# p = Person()
# print(p.name)

# # public:
# class Person:
#     name = "mayaz"
   

# p = Person()
# print(p.name)

# Inheritance:
# single inheritence:
# class Car:
#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod
#     def stop():
#         print("stopped")

# class Toyota(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = Toyota("fortuner")
# car2 = Toyota("supree")

# print(car1.name,car2.name)
# car1.start()

# mutilevel inheritance:
# class Car:
#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod
#     def stop():
#         print("stopped")

# class Toyota(Car):
#     def __init__(self,name):
#         self.name = name

# class fortuner(Toyota):
#     def __init__(self,type):
#         self.type =type

# car1 =fortuner("diesel")
# car1.start()

# multiple inheritance:

class Car:
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("stopped")

class bike:
    def __init__(self,name):
        self.name = name
        print("hello bike")

class Uber(Car, bike):  # Multiple inheritance from Car and bike
    def __init__(self, call, name):  # Accept both 'call' and 'name' for Uber
        bike.__init__(self, name)  # Initialize the bike class
        print("hello, I'm Uber, call received:", call)

# Create an instance of Uber
u1 = Uber('Need a ride?', 'Ducati')

# Accessing the 'name' attribute from bike class
print("Bike name:", u1.name)

# Calling Car's static methods
u1.start()
u1.stop()
