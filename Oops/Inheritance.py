##Inheritance Implementation ##

class GrandFather:
    def __init__(self,name,age,work):
        self.name = name
        self.age = age
        self.work = work
        self.painting = 1


    def display(self):
        print(f"Father name is {self.name} and age is {self.age}, he is working as a {self.work}")



# f = GrandFather("Ramesh",20, "Teacher")
# f.display()


class Father(GrandFather):
    # def __init__(self,name,age,work):
    #     self.name = name
    #     self.age = age
    #     self.work = work
    gym = 1

    def display(self):
        print(f"he is good in gym {self.gym} and painting {self.painting}")

# m = Father("Surya", 21, "Principle")
# m.display()


class Child(Father):
    def child_display(self):
         print(f"he is good in gym {self.gym} and painting {self.painting}")
    

child1 = Child("kk", 10, "study")
child1.display()
child1.child_display()