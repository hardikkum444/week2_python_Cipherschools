# Functions practice 

# a=input("enter any parameter ")
# def last_char(name):
#     return (a[-1])

# b=("input any parameter ")
# print(last_char(b))

# or we can do this by a much simpler method

# def last_char(name):
#     return (name[-1])

# name=input("What is your name? ")
# print(last_char(name))

# odd or even fumction

# def odd_even(number):
#     if number%2==0:
#         return('the number is even ')
#     else:
#         return('the number is odd ')

# number=(int(input('Eneter any random numeber ')))
# print(odd_even(number))

# or an easiser more shorter way

# def odd_even(num):
#     if num%2==0:
#         return "even"
#     return "odd"


# or the most pythonic way

def even(num):
    return num%2==0

num=int(input())
print(even(num))

# The above syntax or formula will give you answer in boolian values 