#variable is just a storage unit(think shopping cart where you put in apple and then twitch it to a banana)

#########################################################

#DATA TYPES IN PYTHON

#Immutable = strings, numbers, tuples
#mutable = dictionaries, lists, sets

###################################

#NUMBERS = integers, floating point numbers, or complex numbers

num1=100
print(type(num1))

#example above is an integer

###type() is a built in function in Python that takes in either one or three parameters. In the example above it is taking in the variable and checking what its associate data structure is (<class 'int'>). It is usually not used for testing. isinstance() is used in testing because it takes into account whether the given object is an instance of a subclass as well.

num2=13.4
print(type(num2))

#above is an example of a floating point number

num3=10-10j
print(type(num3))

#above is an example of a complex number (real and an imaginary part of a number = complex number)

######################################

#STRINGS = anything inside single or double quotes

#how can we extract single characters in string?

str1="this is a string"

#to extract the first two characters from string above you would:

str1[0:2]

print(str1[0:2])

#to extract the last two characters from string above you would:

str1[-2:]

print(str1[-2:])

######################################

#TUPLES = collection of immutable python object inside parathesis
#elements in tuple can be of the same data type or of a different data type

tup1 = ("this", "is", "a", "tuple")

print(tup1)

#access first element

tup1[0]

#extract last element

tup1[-1]

######################################

#LISTS = ordered collection of an elements

my_list = ['python', 'vscode', '11', '12']


#extract first element

my_list[0]

print(my_list[0])

#add element while removing another

my_list[1] = 'hippy'
my_list

print(my_list)

#finding the length of the list

print(len(my_list))

#reverse order

my_list.reverse()

print(my_list)

###################################

#SETS = unordered and unindexed items

#every element in set is unique and does not contain duplicate values
#can be used in mathmatical calcs such as union, intersection, and differences
#if there are duplicate values they will be removed when variable is called
# use <variable>.add('<added_element>') to add element to set
# use <variable>.union('<variable_of_set_that_will_connect>')
# .instersection to return intersection of two sets
# .different returns one set (one in parathesis)

####################################

#DICTIONARIES = unordered collection of data that is stored in key : value pairs 
#key is not mutable and value can be of any type

Dictionary = {'britt':'human', 'trucker':'dog'}

#how to change value
Dictionary['britt'] = 'loser'

print(Dictionary)

#how to access one value
print(Dictionary['britt'])

#how to remove values
del Dictionary['britt']

print(Dictionary)

#######################################

#CONDITIONAL STATEMENTS

A=5
B=10

if A>B:
    print("Hello")
elif B>A:
    print("Hello world")
else:
    print("Hello programmers")

###If statement: Firstly, “if” condition is checked and if it is true the statements under “if” statements will be executed. If it is false, then the control will be passed on to the next conditional statements.

###Elif statement: If the previous condition is false, either it could be “if” condition or “elif” after “if”, then the control is passed on to the “elif” statements. If it is true then the statements after the “elif” condition will execute. There can be more than one “elif” statement.

###Else statement: When “if” and “elif” conditions are false, then the control is passed on to the “else” statement and it will execute.

######################################




