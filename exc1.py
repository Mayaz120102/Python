class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} {self.age}"

# with str

p1 = Person("mayaz",22)  
# print(p1.name,p1.age) without str 

print(p1)  
