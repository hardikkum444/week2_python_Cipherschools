# def func():
#     x=7
#     return x

# def func1():
#     print(x)
#  will not work as x is not a global variable, its a local variable not a global variable

#  neither will it print(x) because of the same reason

# x=5 # global variable 
# def func():
#     x=7
#     print(x) #local variable

# func()
# print(x)

# here it is clearly visible


# to change the value of global x

x=5
def func():
    global x
    x=7
    print(x)

func()
print(x)