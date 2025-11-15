def squares_using_generator(num):
    for i in range(1,num+1):
        yield i*i
        
for number in squares_using_generator(7):
    print(number)