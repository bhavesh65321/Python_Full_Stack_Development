##Inheritance Implementation ##

class GrandParent:
    def __init__(self,name : str,age : int,work : str) -> None:
        self.name : str = name
        self.age : int = age
        self.work : str = work
        self.painting : bool = 1


    def display(self):
        print(f"GrandParent name is {self.name} and age is {self.age}, he is working as a {self.work}")



# f = GrandFather("Ramesh",20, "Teacher")
# f.display()
## using super() method we can call the parent class constructor/initialization, and we can add more attributes to the child class
## we can use super() method to call the parent class method
## we can use parent class name to call  the parent class method in child class

class Parent(GrandParent):
    def __init__(self,name : str,age : int,work : str,gym : bool) -> None:
        #GrandParent.__init__(self,name,age,work)
        super().__init__(name,age,work)
        self.gym : bool = gym
        GrandParent.display(self) ## forcing to call the parent class method

    def display(self):
        print(f"he is good in gym {self.gym} and painting {self.painting}")

m = Parent("Surya", 21, "Principle", 1)
m.display()


class Child(Father):
    def __init__(self,name : str,age : int,work : str,gym : bool) -> None:
        super().__init__(name,age,work,gym)
    def child_display(self):
         print(f"he is good in gym {self.gym} and painting {self.painting}")
    

child1 = Child("kk", 10, "study")
child1.display()
child1.child_display()