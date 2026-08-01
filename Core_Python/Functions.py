"""
Functions - A function is a block of code which only runs when it is called. it can help us not to write same code again and again. its memory efficient.
a = 5
x = a
a = "string"
x = a
"""

# def Incremental(x):   # fun defination
#     for i in range(10):
#         print("counter is", i*x)

# Incremental(5) # this is function calling where we can pass arguments if needed
# Incremental(10)
# Incremental(15)


# x = 5
# for i in range(10):
#     print("counter is", i*x)
# x = 10
# for i in range(10):
#     print("counter is", i*x)
# x = 15
# for i in range(10):
#     print("counter is", i*x)

#default paramter


# def Incremental(x):   # fun defination
#     for i in range(10):
#         print("counter is", i*x)

# Incremental() #fun calling


# def myName():
#     print("My Name is X")

# myName()

#positional arguments and keyword arguments

###positional arguments
###Keyword Arugments

# def myBioData(fName, lName,City,clss,Name):      # Name = Bhavesh, City = "Sanchore", clss = 8
#     print("My Name is : ",Name)
#     print("My city is : ", City)
#     print("My class is : ", clss)
#     print("My Full Name is :", fName.strip() +" "+ lName.strip())

# myBioData("Bhavesh ", "Soni",Name = "Bhavesh",City = "Sanchore",clss = 8) #positional arguments and keyword arguments, in case when use both arguments in the same functional call then we write postional arguments first then keyword arguments.


# # *args (positional arguments) and **kwargs (keyword arguments)
# #By default, a function must be called with the correct number of arguments.However, 
# # sometimes you may not know how many arguments that will be passed into your function. 
# # *args and **kwargs allow functions to accept a unknown number of arguments.

# def myBioData(*ListValue): 
#     print(ListValue, type(ListValue))     # Name = Bhavesh, City = "Sanchore", clss = 8
#     print("My Name is : ",ListValue[2], "My city is : ", ListValue[3], "My class is : ", ListValue[4])
#     print("My Full Name is :", ListValue[0].strip() +" "+ ListValue[1].strip())

# myBioData("Bhavesh ", "Soni", "Bhavesh", "Sanchore",8, "UG", "India") #arugments -> convert into tuple -> tuple will pass as paramter list to the func


#**keyword arbitary arguments (**kwargs)

# def myBioData(**Dictionary): 
#     print(Dictionary, type(Dictionary)  )   # Name = Bhavesh, City = "Sanchore", clss = 8
#     # for i, j in Dictionary.items():
#     #     print(i, "  ",j)
#     print("My Name is : ",Dictionary['Name'], "My city is : ", Dictionary['City'], "My class is : ", Dictionary['clss'])
#     print("My Full Name is :", Dictionary['fName'].strip() +" "+ Dictionary['lName'].strip())

# myBioData(fName = "Bhavesh ", lName = "Soni", Name = "Bhavesh", City =  "Sanchore", clss = 8, ED = "UG",  Ctry = "India") # keyword arugments -> conver into dictionary -> dictionary will pass as paramter list to the func

# # Dictionary

# a = {
#     'fName': 'Bhavesh ', 
#  #key      value
#  'lName': 'Soni', 
#  'Name': 'Bhavesh', 
#  'City': 'Sanchore', 
#  'clss': 8, 
#  'ED': 'UG', 
#  'Ctry': 'India',
#  '1' : "Test",
#  }


# ColorOfCar = {
#         "Red": "34X30",
#     "White": "324xv"
# }

# print("Yes we find out", ColorOfCar["Red"])

# A = ["Red","Yellow","Orange"]
# for i in range(len(A)):
#     print(i,A[i])
#     if A[i] == "Orange":
#         print("Yes, we find the color")
#         break
#     else:
#         print("We didn't able to find")


# ### Scope Concept - local Scope and Global Scope
# x = 300 #Global 
# def myMath(): #functions and Methods are same
#     global y
#     y = 400 #Local variable
#     print(x+y)
#     def myInnerMath():
#         z = 120
#         print("After this executed",x*y*z)
#         def mydepathInnerMath():
#             print("yes")
#         mydepathInnerMath()
#         print("fun 3 execution completed")
#     print("Before myInnerMath")
#     myInnerMath()
#     # print(y)

# myMath()
# print(y)


# function 1 - myMath -> myMath excution started -> whenever we hit line 123, then myMath execution get stopped it will wait until myInnerMath or child function execution is not getting completed
# then once that execution completed then again pending fun execution get started

##Lambda function - Lambda function is small anonymous functions - IMP
## In python, anonymouns function is a function that is defined without a name. while normal functions are defined using the def keyword in python
##anonymous function are define using the lambda keyword

##Syntax Lambda arugments : experssions

# def myMath(a,b):
#     print(a+b)

x = lambda a,b : a + b


### private protected public 

def myMathOperation(a,b,c):          #this void function - means not returning anything
    return  lambda a,b,c : a + b + c
    y = lambda a,b,c : a*b*c
    z = lambda a,b : a/b
    print(x,y,z)

ReturnValue = myMathOperation(10,20,30)
ReturnValue = myMathOperation(10,20,10)

print(ReturnValue)


## write lambda function for all mathematices operation - in nested form 
## print square of each number from 1 to 100 using lambda func







        





