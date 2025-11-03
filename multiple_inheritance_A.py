class A:
    def func1(self):
        print("This is the function 1 from class A")
class B:
    def func2(self):
        print("This is the function 2 from class B")
class C(A,B):
    def func3(self):
        print("This is the function 3 from class C")
obj=C()
obj.func1()
obj.func2()
obj.func3()
obj1=A()
obj1.func1()
obj2=B()
obj2.func2()