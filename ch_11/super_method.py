class mittal:
    compney='msi'
    def __init__(self):
        print("mittal: you have no leptop")
    def computer(self):
        print("mittal: i have acer computer at my home.")
    def spacification(self):
        print("mittal: it hase 8gb ram and 1TB storage. it hase intal i7 processer in it")
class krishna:
    compney='intel'
    def __init__(self):
        print("krishna: you have no pc")
    def computer(self):
        print("krishna: i have asus leptop at my home.")
    def spacification(self):
        print("krishna: it hase 4gb ram and 1TB storage.it has intal performance processer in it.")
class shyam(mittal):
    def __init__(self):
        super().__init__()
        print("shyam: i have both leptop and pc.")
    def computer1(self):
        super().computer()
        print('shyam: and i also have hp leptop')
    def spacification1(self):
        super().spacification()
        print("shyam: my leptop has hase 8gb ram and 1TB storage.it has rizen 5 processer in it.")
m=mittal()
k=krishna()
s=shyam()
s.computer()
s.spacification()