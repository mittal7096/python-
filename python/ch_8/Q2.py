a=int(input("enter the value to convert frome celcius to fahrenheit:-"))
def convert(int1):
    con=(int1*(9/5)+32)
    return con
fahrenheit=convert(a)
print("celcius=",a ,"converted to fahrenheit is:-",fahrenheit)