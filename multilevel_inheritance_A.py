class A:
    def func1(self):
        print("class 1 function is executed successfully")
class B(A):
    def func2(self):
        print("class 2 function is executed successfully")
class C(B):
    def func3(self):
        print("class 3 function is executed succcesfully")
obj1=C()
obj1.func1()
obj1.func2()
obj1.func3()
obj2=B()
obj2.func1()
obj2.func2()
obj3=A()
obj3.func1()