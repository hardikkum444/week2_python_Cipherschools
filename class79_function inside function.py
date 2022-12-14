def greater_than(a,b):
    if a>b:
        return a 
    return b 




def new_greatest(a,b,c):
    bigger=greater_than(a,b)
    return greater_than(bigger,c)

print(new_greatest(100,20,1000))