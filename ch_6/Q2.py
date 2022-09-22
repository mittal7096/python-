maths=int(input("enter your marks in maths:-"))
english=int(input("enter your marks in maths:-"))
physic=int(input("enter your marks in maths:-"))
boop=int(input("enter your marks in maths:-"))

if(maths>33):
    print("you are passed in maths:=",maths)
else:
    print("you are faileld in maths",maths)

if(english>33):
    print("you are passed in english:=",english) 
else:
    print("you are faileld in english",english)

if(physic>33):
    print("you are passed in physic:=",physic)
else:
    print("you are faileld in physic",physic)

if(boop>33):
    print("you are passed in boop:=",boop)
else:
    print("you are faileld in boop",boop)
a=maths+english+physic+boop
if((a/4)>40):
    print("you are passed with ",(a/4),"marks.")
else:
    print("you are failed with ",(a/4),"percentage")

                        #OR

maths=int(input("enter your marks in maths:-"))
english=int(input("enter your marks in maths:-"))
physic=int(input("enter your marks in maths:-"))
boop=int(input("enter your marks in maths:-"))

if(maths>33 and physic>33 and english>33 and boop>33):
    print("you are passed ")
else:
    print("you are failed")