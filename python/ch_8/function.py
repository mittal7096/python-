def per(marks):
    y=((sum(marks)/400)*100)
    return y
a=int(input("enter your marks in maths"))
b=int(input("enter your marks in boop"))
c=int(input("enter your marks in physic"))
d=int(input("enter your marks in BDE"))
e=int(input("enter your marks in maths"))
marks1=[a,b,c,d,e]
percentage=per(marks1)
print("you got :-",percentage,"in your exam")