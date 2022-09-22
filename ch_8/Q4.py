# Q4. write a recursive function to calculate the sum of first n natural number.

a=int(input("enter the number:-"))
def rec(n):
    if n==0:
        return n
    n=n+rec(n-1)
    return n
b=rec(a)
print("sum of natural number is :-",b)
