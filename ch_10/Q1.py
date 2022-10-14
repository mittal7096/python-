class programmer:
    compney='microsoft'
    def __init__(self,name,sallery,region):
        self.name=name
        self.sallery=sallery
        self.region=region
    def getdata(self):
        print(f'your name is:-{self.name}')
        print(f'your sallery is {self.sallery}')
        print(f'your region is {self.region}')

mittal=programmer('mittal',230000,'india')
mittal.getdata()


