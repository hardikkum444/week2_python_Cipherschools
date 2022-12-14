def greater_than(a,b):
    if a>b:
        return a 
    return b 

a=int(input("Enter first number "))
b=int(input("Enter second number "))
greater=greater_than(a,b)
print(f'{greater} is the bigger number ')