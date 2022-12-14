def greatest (a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    return c

a=int(input("enter a number "))
b=int(input("enter a number "))
c=int(input("enter a number "))

print(f'The greatest number out of the three is {greatest(a,b,c)}')