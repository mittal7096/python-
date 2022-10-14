class employee:
    compney='intel'
    sellery=23000
    region='india'
    def changesallery(self,sel):#this is a first methode to change value of class attrebute.
        self.__class__.sellery=sel

    @classmethod# this is second method to change calue of class attrebute.
    def changesallery1(self,sel):
        self.sellery=sel

e=employee()
# print(e.sellery)
e.changesallery(96666)
print(employee.sellery)
# print(e.sellery)
e.changesallery1(23233)
# print(e.sellery)#hear class attrebute will not change.
print(employee.sellery)