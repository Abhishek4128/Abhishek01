# By Using Constructor If We Create Any Object It will Automatically Call The Constructor Function We Need Not To Call Externally
class student:
    a=45
    def __init__(self,name):
        self.name = name
        print(f"My Name Is {self.name} I Am In Constructor And Executing It!")
        self.b=50
    def add(self):
        return self.a+self.b
obj1=student("ram")
print(obj1.add())