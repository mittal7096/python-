from operator import truediv


spam=input("enter your text:-\n")
if("make a lot of money" in spam):
    spam=True
elif("buy now" in spam):
    spam=True
elif("subscribe this" in spam):
    spam=True
elif("click this" in spam):
    spam=True
else:
    spam=False
if(spam):
    print("it is a spam comment.")
else:
    print("it is not a spam comment.")
    