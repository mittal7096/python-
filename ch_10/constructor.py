class employe():

    def employ(self):
        print('your work is present on the desk of your frend shebu.')
        print('your name is:-',self.name)
        print('your sallery is:-',self.sallery)
        print('your country is:-',self.country)

    def __init__(self,name,sallery,contry):
        self.name=name
        self.sallery=sallery
        self.country=contry

        print('helow sir how are you')
mota = employe('mittal',45000,'india')
mota.employ()
