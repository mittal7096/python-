maths=int(input("enter your marks in maths:-"))
english=int(input("enter your marks in english:-"))
physic=int(input("enter your marks in physic:-"))
boop=int(input("enter your marks in boop:-"))
a=maths+english+physic+boop
marks=((a/320)*100)
if(marks==100 and marks>90):
    print("you got 'A' grade and you percentage is:-",marks)
elif(marks<90 and marks>80):
    print("you got 'B' grade and you percentage is:-",marks)
elif(marks<80 and marks>70):
    print("you got 'C' grade and you percentage is:-",marks)
elif(marks<70 and marks>60):
    print("you got 'D' grade and you percentage is:-",marks)
elif(marks<60 and marks>50):
    print("you got 'E' grade and you percentage is:-",marks)
elif(marks<50):
    print("you got 'F' grade and you percentage is:-",marks)
else:
    print("you have not enter valid marks.")