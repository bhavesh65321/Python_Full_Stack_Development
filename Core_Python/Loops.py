"""
Loops
1. While Loop - we can execute set of statements as long as a condition is true
2. do while loop
3. For Loop - we can execute a set of statements a specific number of times

i = 0
b = 0
do {
print(i, b)
statement
}
while(condition);
{
statments
}
"""

# i = 0 
# b = 0  # 0 means False, except 0 every other integer value is always True
## Break, Continue

# while(i < 10): 
#     i += 1
#     if i == 3:  #i want print only value 3 
#         print(i, "Yes")
#     else:
#         continue #after continue keyword it will not execute further line of code for that iteration, we can step the current iteration and continue with the next.
#         print(i,"No")    
# print("We found the address")  
#  


a = [1,2,3,4,5,6,7,8,9]

lower_limit = 0
upper_limit = len(a)


# for i in a: # direct value
#     print(i)

#range(lower limit, upper limit).    [lower, upper)
# for i in range(1, 10):
#     print(i)

#1 - left to right
# -1 - right to left
# for i in range(lower_limit,upper_limit,1): # through indexes
#     print(a[i])

# for i in range(upper_limit-1,lower_limit-1,-1): # through indexes
#     print(a[i])


# a = "Banana"

# for i in a:
#     print(i)

# print("Please provide input")
# n = int(input())
# print(n)


a = ["Apple", "Banana","Cake","Sweets", 1, 2, 9, "Mango", 10.15]

#simple print

# for i in a:  # i is holding value from list
#     print(i)

i = 0
j = len(a)

# for i in range(0,j): # i is holding index of the list
#     print("index number- ", i,"=", a[i])

for i in range(j-1,i-1,-1):
    print("index number- ", i,"=", a[i])

# give me sum of even number (0-100)
# give me sum of odd number (50-150)
# find how many even number is there in the list [2,7,9,11,12,15,19]












  

