a = int(input("enter the 1'st number:-"))
b = int(input("enter the 2'nd number:-"))
c = int(input("enter the 3'rd number:-"))
def max(int1,int2,int3):
    if int1>int2:
        maxe=int1
    else:
        maxe=int2
    if int3>maxe:
        maxe1=int3
    else:
        maxe1=maxe
    if maxe>maxe1:
        return maxe
    else:
        return maxe1
m=max(a,b,c)
print("maximum number is :-",m)