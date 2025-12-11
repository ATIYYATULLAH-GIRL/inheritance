class Person:
    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print("Your name is", self.name)
        print("Your idnumber is", self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)
obj=Employee("Rahul",88656,200000,"Intern")
obj.display()