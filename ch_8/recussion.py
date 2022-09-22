'''n=int(input("enter the number:-"))
def fac(n1):
    p=1
    for i in range(n1):
        p=p*(i+1)
    return p
if n==1 or n==0:
    print(1)
print(fac(n))'''
#   NOW WITH RECUSSIVE METHORD.
'''
def rec(n1):
    if n1==1 or n1==0:
        return 1
    return n1*rec(n1+1)
n=int(input("enter the number:-"))

print(rec(n))
'''
            # OR

n1=int(input("enter the number:-"))
def ffac(n):
    if n==1 or n==0:
        return 1 
    n=n+ffac(n-1)
    return n
a=ffac(n1)
print(a)

