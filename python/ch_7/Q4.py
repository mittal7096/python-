a=int(input("enter the number:="))
prime=True
for i in range(2,a):
    if a%i==0:
        prime=False
        break
if prime:
    print("this is a prime number.")
else:
    print("this is not a prime number.")
