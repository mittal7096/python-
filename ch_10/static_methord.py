class employe:
    compney=' google'

    # def __init__(self):
    #     self.sallery = userinput2
    #     self.age = userinput4
    #     self.living = userinput3
    #     self.name = userinput1

    def employeDetail(self):
        print(f'name of the employ:-{self.name}')
        print(f'compney name:-{self.compney}')
        print(f'age of the {self.name}:-{self.age}')
        print(f'sallary of the {self.name}:-{self.sallery}')

a=input("enter '1' to enter employ detail\nenter '2' for exit:-")
if a=='1':
    userinput1 = input("enter the name of user:-")
    userinput2 = input("enter the sallery of user:-")
    userinput3 = input("enter the living of user:-")
    userinput4 = input("enter the age of user:-")
    aa=employe()
    aa.name = userinput1
    aa.sallery = userinput2
    aa.living = userinput3
    aa.age = userinput4
elif a=='2':
    print('thanks you for giving your precies time :).')

chakeinput1=input("enter the name of the employ of which you want the detail:-")
if chakeinput1==userinput1:
    aa.employeDetail()
else:
    print(f'entered employ is not working in {employe.compney}')
