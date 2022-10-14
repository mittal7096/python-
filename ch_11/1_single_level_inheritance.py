class employe:
    compney="google"
    def showData(self):
        print("i am a employ of google.")
class statup(employe):
    compney = "youTube"
    def getdata(self):
        print("i am a employ of youTube")
e=employe()
e.showData()
s=statup()
s.showData()
s.getdata()