class first:
    def function1(self):
        print("This is Function1 From Class first")
class second(first):
    def function2(self):
        print("This is Function2 From Class second")
obj1=second()
obj1.function2()
obj1.function1()
obj2=first()
obj2.function1()