class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print(f"{self.name} doing general employee task!")
class manager(employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def work(self):
        print(f"{self.name} manages the team of size {self.team_size}")
class developer(employee):
    def __init__(self, name, salary,prglang):
        super().__init__(name, salary)
        self.prglang=prglang
    def work(self):
        print(f"{self.name} is coding on {self.prglang}")
e1=employee("john",50000)
m1=manager("ram",75000,10)
d1=developer("rahul",100000,"pyhton")
for emp in [e1,m1,d1]:
    emp.work()