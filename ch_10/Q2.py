class calculator:
    def __init__(self,number1):
        self.number1=number1

    def square(self):
        print(f'square of the given {self.number1} is {self.number1*self.number1}')
    def cube(self):
        print(f'cube of the {self.number1} is {self.number1*self.number1*self.number1}')
    def squareRoot(self):
        print(f'square root of the {self.number1} is {self.number1 **0.5}')

a=int(input("enter the number :-"))
cal=calculator(a)
cal.square()
cal.cube()
cal.squareRoot()
