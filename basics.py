# print("hello world! this is mayaz")
# print(8/3)
# name ="mayaz"
# age = 23

# print(name,age)
--To print : print()

#Variables:

--ariables do not need to be declared with any particular type, and can even change type after they have been set.Variable names are case-sensitive.
--If you want to specify the data type of a variable, this can be done with casting
--can get the data type of a variable with the type() function.
--String variables can be declared either by using single or double quotes:
--Python allows you to assign values to multiple variables in one line:

#Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

#Datatypes in python :

--Text Type:	str  : ("Flagman", 'hello world';)
--Numeric Types:	int(-ve,+ve, 0), float(having decimal point), complex
--Sequence Types:	list, tuple, range
--Mapping Type:	dict
--Set Types:	set, frozenset
--Boolean Type:	bool(true , flase)
--Binary Types:	bytes, bytearray, memoryview
--None Type:	NoneType

#Setting the Data Type:

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType

Creating a Comment
Comments starts with a #, and Python will ignore them

#modify string 
--upper(), lower(), stip(), slice(),replace(),split(","),F-String

#escape characters

\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

#Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	Example	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

#Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)

#Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y

#Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

--add(append(),insert(),extend,)
--remove,pop(ind)/pop(without ind will pop the last),del,clear

--newlist = [expression for item in iterable if condition == True]

--thislist.sort()    --thislist.sort(reverse = True)

#python tuples
Tuple
--Tuples are used to store multiple items in a single variable.

--Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

--A tuple is a collection which is ordered and unchangeable.

--Tuples are written with round brackets.

#Python Collections (Arrays)
There are four collection data types in the Python programming language:

-List is a collection which is ordered and changeable. Allows duplicate members.
-Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
-Dictionary is a collection which is ordered** and changeable. No duplicate members.


#Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary


# ============ -0- ===================

#Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates

# Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others

# ======================== 0 ========================

# Python Loops
Python has two primitive loop commands:

while loops
for loops:
  --A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

----This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

----With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

for el in 


# function in python :

# Files in python :
f = open("path","mode")
mode = r,w,x,a,b,t,+
read a file:
--f.read --> to read a entire file
--f.readline()--> reads one line at a time



# extra--------------------
In Python, list, tuple, and dictionary have different time complexities for their operations, and their use cases differ depending on the situation. Here’s a breakdown of their time complexities and when they are most applicable:

1. List (list)
A list is a dynamic array in Python that is mutable, meaning you can add, remove, or modify elements.

Time Complexity for Common Operations:
Access by index: O(1) (constant time)
Search (in operation): O(n)
Append (at the end): O(1)
Insert (at arbitrary position): O(n) (since elements need to be shifted)
Delete by index: O(n) (shifting elements)
Pop (remove last element): O(1)
Applicability:
Use list when you need a collection of elements that may change in size (mutable).
It is ideal when you want to frequently access elements by index, append to the list, or need to maintain an ordered collection.
2. Tuple (tuple)
A tuple is an immutable sequence in Python, meaning once it is created, it cannot be modified.

Time Complexity for Common Operations:
Access by index: O(1) (same as list)
Search: O(n)
Creation: O(n)
Applicability:
Use tuple when you have a fixed set of elements that shouldn't change (immutable).
It is preferable when immutability provides safety or optimization, such as for keys in dictionaries or for representing fixed collections like coordinates or configurations.
3. Dictionary (dict)
A dict is a hash map or associative array that stores key-value pairs and allows for fast lookups, insertions, and deletions by key.

Time Complexity for Common Operations:
Access by key: O(1) average (but O(n) in worst cases with hash collisions)
Search (by key): O(1) average
Insert/Update: O(1) average
Delete by key: O(1) average
Applicability:
Use dictionary when you need to map a set of unique keys to values.
It is ideal when you want to access values quickly by a specific key (constant-time lookup) or when the order of elements doesn't matter as much as efficient key-value operations.
Which One to Use in Which Situation:
Use list when:

You need a dynamic, mutable collection of elements.
You want to maintain order and need to frequently access elements by index.
You don't need fast lookups by key, but rather just need an ordered sequence.
Use tuple when:

You need an immutable collection of elements.
Safety and memory optimization are important.
The collection is fixed, like geographic coordinates, or will be used as a key in a dictionary.
Use dict when:

You need fast lookups by key.
You need to associate unique keys with values, such as a phone book, an index, or a cache.
Keys need to be immutable, but values can change.
Each data structure has its strengths depending on the context, so choose based on whether you prioritize immutability, fast lookups, or dynamic resizing.

--Summary of Total Time Complexities:
List: O(n) on average.
Tuple: O(n) on average.
Dictionary: O(1) on average, but O(n) in the worst case (due to hash collisions).