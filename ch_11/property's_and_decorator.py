class google:
    sallery=3000
    bonussallery=200
    @property
    def addition(self):
        n=self.sallery+self.bonussallery
        return n
    @addition.setter
    def addition(self,val):
        self.bonussallery=val-self.sallery

g=google()
aa=int(input('enter the sallery you want:-'))
g.addition=aa
f=g.sallery
print(f'sallery = {f}')
h=g.bonussallery
print(f'bonus sallery = {h}')
i=g.addition
print(f'total sallery = {i}')

