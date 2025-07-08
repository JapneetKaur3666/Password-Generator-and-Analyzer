import random
import string

def password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    word=''.join(random.choice(chars) for i in range(length)) #random.choice(chars) picks one random character from the chars string.
    return word     #for i in range(length) loop that runs length times #''.join(..)joins list of characters into a single string without spaces.
def count(p):
    parts=list(p) #breaks string to list where each element is single character from the original string, preserving their order.
    lcount=dcount=pcount=0
    for j in parts:
        if(j in string.ascii_letters):
            lcount+=1

        elif(j in string.digits):
            dcount+=1
        elif(j in string.punctuation):
            pcount+=1 
    print(f"This pswd contains {lcount} letters,{dcount} digits and {pcount} symbols.")
length=int(input("enter length of pswd :"))
p=password(length)
print("Your pswd is ",p)
count(p)
