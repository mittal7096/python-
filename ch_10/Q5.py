

# write a class train which has methods to book a ticket,get status (no of seats) ane get fare information of train running under
# indian railways.
class train:
    def __init__(self,name,time,seat,price):
        self.name=name
        self.time=time
        self.seat=seat
        self.price=price

    def ticket(self):
        print(f'name of the train is {self.name}')
        print(f'it will arived at {self.time}')
        print(f'no of seat {self.seat}')
        print(f'price of the ticket if {self.price}.Rs')
    def bookticket(self):
        bookticket = input('if you want to register the ticket type yes:-')
        if bookticket =='yes':
            print(f'your ticket is booked.on seat no {self.seat-1}.')
            self.seat=self.seat-1
        else:
            print(f'{bookticket} this seat no is not avalable in this train ')
    def seatavalable(self):
        print(f'no of seats are avalable:-{self.seat}')

name='rajdhani'
time='3:30pm'
seats=150
price=350
imfo=train(name,time,seats,price)
imfo.ticket()
noofseat=int(input('enter the no of seats you eant to register'))
for i in range(noofseat):
    imfo.bookticket()
imfo.seatavalable()

