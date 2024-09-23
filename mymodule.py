# def greeting(name):
#     print("hello, " + name)

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

#  There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# import platform

# x = dir(platform)
# print(x)

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

# Example
# Create an alias for mymodule called mx:

# import mymodule as mx

# a = mx.person1["age"]
# print(a)
# The module named mymodule has one function and one dictionary:

# def greeting(name):
#   print("Hello, " + name)

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }
# Example
# Import only the person1 dictionary from the module:

# from mymodule import person1

# print (person1["age"])


# import datetime
# x= datetime.datetime.now()
# print(x)