# print("Hello World")

#What is python ??

##Compile --> 
##Interpreter ->

##How Python Program get execute ##

# x = 10
# y = 20  ---> object(10), object (20). --> binary number (machine language) --> 

# print(x+y)

#Variables
# a = 10
# b = "10"
# print(type(a))

# int n;
# n= "test"

#Python is not allow to convert text string (characters) into integer directly we can use ASCII method to convert.

# print(a+int(b))

# print(str(a)+b)

#How we define VariableNames
#1.CamelCase - Each word except first letter of word start with a Capital letter.

"""
myFullName = "Bhavesh",
fullName
schoolPassowrd,
happyNewYear
"""

#2.Pascal Case - 
"""
MyFullName,
FullName,
SchoolPassword,
HappyNewYear
"""

#3 snakecase -
"""
my_full_name,
full_name,
school_password,
happy_new_year
"""

#How we can define mutiple variables with single value or multiple value
# a = "Bhavesh"
# b = "Bhavesh"
# c = "Bhavesh"

# a = b = c = d = "Bhavesh"
# print(a,b,c,d)

# a = b = c = d = "A","B","C","D" --> Complete Object
# print(a,b,c,d)

# a,b,c,d = "A","B","C",1. 
# print(a,b,c,d)

"""
Case_Senitive

"""

"""
Comments

"""

"""
Identation
"""

"""
Data Types

Numeric - int (positive,negative,zero), float (any value with decimal), complex (1+2j)
Sequence - list (its array), str, tuple 
Array is a concept but list is python's functionality.

list - A list is an ordered, mutable(allow to update) collection that can store multiple items of different data types.

a = [1,2,3,4,5]
print(a)
#[1,2,3,4,5]
a = [1,2,3,4,5]
a = [1,2,3,4,5,6] #add
a = [1,2,4,5,6] #delete
a = [1,2,4,8,6] #update

tuple - A tuple is an ordered, immutable(not allow to update) collection that can store multiple items of different data types.
    a = (1,2,3,4,5)
    print(a)
    # (1,2,3,4,5)
   a = (1,2,3,4,5) #add throw the error
"""

# a = [1,2,3,4,5]
#     #0,1,2,3,4
# print(a)
# a.append(6) #Add
# a[1] = 10
# print(a)
# a[3] = 45
# print(a)
# # a[7] = 80
# # print(a)
# print(len(a))


# print(type(a))

# b = list(tuple([1,2,3,4,5]) )
# c = (1,2,3)
# #b.append(8) #its breaking program from here
# b[3] = 55
# print(b)

# c = set(["A","B","C"]) #unordered
# print(c)
# print(c)
# print(c)

#range - immutable,ordered

#range(1,6) ---> [1,6) it will 
#1,2,3,4,5

#range(1,11) --->
#1,2,3,4,5,6,7,8,9,10

# numbers = range(3,12)

# for i in numbers:
#     print(i)



c = """
String - sequence of charcters support single quote, double quote and multiline string

a = 'Test'
b = "TestNew"

String its represent as arrays, by default index start with zero


#Slicing

#positive indexing
 

"""
# print(c)

# A = "HappyNewYear" 
#         #   -4-3-2-1
               

# print(A[5:8])

# #Negative indexing - indexing will get start from the end , but while slice the string we will follow left to right pattern.

# print(A[-4:-1])

# #Steps Hpye

# # A[start_index : ending_index : steps = 1]

# print(A[2:8:2])

# #ReverseString using slice

# print(A[::-1])

#in or not in 

A = "my name is ramesh kumar"

# print("name" in A)
# print("test" in A)

print(" my name is ramesh kumar" in A)


#String Concentation
# a = "Bhavesh"
# b = "soni"

# print(a+"_"+b)


#String Concentation - with integer value with type conversion

#The Format() function takes multiples arguments and placed in placeholder its using indexing to place multiples arguments

# A = "my name is ramesh {0} kumar and my age is {1}"
# age = 35
# c = 12
# b = 16

# print(A.format(b,c))


# format(1- 0 index , 2 - 1 index ). --->

# A = "My Name is {0} and I am living in {1}, Currently I am study in class {2} and my age is {3}"
# b = "Ramesh"
# c = "Rajasthan"
# d = 8
# e = 28

# print(A.format(b,c,d,e))

"""
b - 0 index
e - 1 index
c - 2 index
d - 3 index
"""

# f = "suresh"
# g = 10
# h = "Dehli"
# i = 33
# print(A.format(f,h,g,i))


"""
# len() - length

"""

A= "abcdef"
# upper()
#lower()
#len()
#replace()
#split()

A = "My name is Suresh" 
# B = A.replace("Suresh","Ramesh")

# print(B)
# print(A)
B = A.split(" ")
print(B)










     

















 