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









