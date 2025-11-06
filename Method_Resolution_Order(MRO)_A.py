class A:
    def show(self):
        print("Function A")
class B(A):
    def show(self):
        print("function B")
class C(B):
    pass
print(C.mro())
print(B.mro())
obj=C()
obj.show()