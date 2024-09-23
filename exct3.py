# polymorphism
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("started")




# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("pending for sail")


# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("taking off")


# c1 = Car("toyotaa","Corola")
# b1 = Boat("titanic","1911")
# p1 = Plane("usbangla","2014")

# # c1.move()
# # b1.move()
# # p1.move()

# for x in (c1,b1,p1):
#     x.move()

# inheritance with polymorphism
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail")

class Plane(Vehicle):
    def move(self):
        print("fly")

c1 = Car("toyotaa","Corola")
b1 = Boat("titanic","1911")
p1 = Plane("usbangla","2014")

# c1.move()
# b1.move()
# p1.move()

for x in (c1,b1,p1):
    print(x.brand)
    print(x.model)
    x.move()