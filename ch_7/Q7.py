# Q.7 write a program to print the following star pattern.
'''         *
         *  *  *
      *  *  *  *  *

for i in range(4):
    if i==1:
        print(" "," ","*")
    elif i==2:
        print(" ","*","*","*")
    elif i==3:
        print("*","*","*","*","*")
'''
        # OR
n=3
for i in range(3):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))


