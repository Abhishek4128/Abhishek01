def factorial_generator(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
        yield factorial
num=int(input("enter a number:"))
for value in factorial_generator(num):
    print(value)