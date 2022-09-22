n=int(input("Enter the Number: "))
for i in range(n):
        if(i in range(1,n-1)):
            print("* ","  "*(n-3),"*")
            continue
        print("* "*n)