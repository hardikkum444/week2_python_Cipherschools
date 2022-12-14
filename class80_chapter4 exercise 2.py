# to find if an inputed word is a palindrome or not:

def palindrome(name):
    return name[::-1]==name

name=input("input name to check if it's a palindrome ")
print(palindrome(name))