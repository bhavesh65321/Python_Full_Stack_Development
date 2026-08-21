class Parent:   ##class implmentation
    pass

child_one = Parent() ##Object creation 

# class Parent:
#     name = "Suresh"  ##class attribute

# child_two = Parent()
# print(child_two.name)

## This is built in class method, which always get execute at the time of object creation or class is being intialized.
##its work like constructors of other languages, at the time object creation we want to initialized some properties and method.

class Person:
    def __init__(self,name,age):  ##this method will get executed at the time object creation it self.
        self.name = name
        self.age = age
        # self.display() ##display(self)
    
    def display(self):
        print(f"My Name is {self.name}, my age is {self.age}")

##self parameter is a reference of the current instance of the class(object)
##self keyword hold the reference of current object, current object holding its own values.


person1 = Person("Ramesh","1")
person2 = Person("Kailash", "20")
person3 = Person("Aakash","25")

print(person1.name)
print(person1.display()) ##display(person1)

# del person1.age
# # print(person1.age)

# print(person2.age)
# print(person1.name)

del person2.name
# print(person2.name)
print(person2)
person2.name = "shivam"
print(person2.name)

"""

Person1 -> [name: "Ramesh"]
Person2 -> [name: "shivam",age: "20"]
Person3 -> [name: "Aakash", age: "25"]


"""








