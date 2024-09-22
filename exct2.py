# inheritance:

# class Person:
#     def __init__(self, firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
    
#     def printname(self):
#         print(self.firstname,self.lastname)

# # derived class
# class Student(Person): 
#     pass

# s1 = Student("abrar", "mayaz")
# s1.printname()

class Person:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self):
        print(self.firstname,self.lastname)
# When we add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
    def __init__(self,firstname,lastname):
        Person.__init__(self,firstname,lastname)
# also can use superfunction  super()

s1 = Student("abrar", "mayaz")
s1.printname()

