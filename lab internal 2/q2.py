import re
n=input("Enter a number: ")
r= re.fullmatch(r'[6-9][0-9]{9}',n)
if(r!=None):
    print("Valid")
else:
    print("Invalid")
email=input("Enter a mail: ")
reg= re.fullmatch(r'[A-Za-z._%+]+@[A-Za-z]+\.[A-Z|a-z]{2,7}',email)
if(reg!=None):
    print("Valid")
else:
    print("Invalid")

name=input("Enter a name: ")
x= re.fullmatch(r'[A-Za-z]{6,100}',name)
if(x!=None):
    print("Valid")
else:
    print("Invalid")