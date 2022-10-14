class employ:
    def name(self):
        print("my name is mittal domadiya.")
class mittal(employ):
    def country(self):
        print("my country name is india.")
class krishna(mittal):
    def state(self):
        print("i live in gujarat.")
e=employ()
m=mittal()
k=krishna()
k.name()
k.country()
k.state()