def swap_case(s):
    lst=[]
    for char in s:
        if char.islower():
            lst.append(char.upper())
        elif char.isupper():
            lst.append(char.lower())
        else:
            lst.append(char)
    return "".join(lst)

if __name__ == '__main__':
    s = input("enter the name:")
    result = swap_case(s)
    print(result)