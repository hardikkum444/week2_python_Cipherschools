n=input("what is your name? ")
temp=""
for i in range (0,len(n)):
    if n[i] not in temp:
        print(f"{n[i]}  {n.count(n[i])}")
        temp+=n[i]