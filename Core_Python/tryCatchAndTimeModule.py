##try - catch block 

"""
try - whatever code we want to execute we will add in try block and try block test code if there any code of errors then it point to except block to handle that error

"""

# try: #it will always test our code based on that except and else block get executed
#     n = int(input("Give input here: "))
# except Exception as e: #whenever there is error in our code then its raise exception and throw that exception
#     print("Something is wrong here",e)
# else: #whenever our code get execute successfully without throwing an error then else block get executed
#     print("Everythings is working fine here")
# finally: #final keyword will always get execute regradless of our code error
#     print("our program get executed")


"""
1. ValueError - if we add wrong type of value then it will handle this error
2. TypeError - its raised when we do some operation where we are adding different type value like adding string value + integer value
3. ZeroDivisionError - its raised when we divided any value with zero
"""

# try:
#     n = input("Give input here: ")
#     a = "Test " + n
#     c = 10/0
# except ValueError:
#     print("this is not number")
# except TypeError:
#     print("operation type is not matching")
# except ZeroDivisionError:
#     print("we should not divided any value with zero")



###Time Module

"""
"""
import time

# current_time = time.time() ##calculate time from since january1, 1970 Unix timestamp
# t1 = time.ctime()
# print(current_time)
# print(t1)


# start_time = time.time()

# n = int(input("give integer input :"))

# for i in range(n):
#     print(i)
# time.sleep(2)

# end_time =time.time()
# print("total time to execute the program",end_time-start_time)

t = time.localtime()

print(t,t.tm_year)





