import random 
# pip install random
import string
# pip install string

pass_list = [x for x in string.printable if x not in string.whitespace] #generates string list that can be used


passwd = "$"
for i in range(12):
    ind = random.randint(0,93) 
    passwd = passwd + pass_list[ind]

passwd = passwd + "@"
print("Your Password is: ",passwd)
