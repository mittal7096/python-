'''
we all have played snake,water gun game in oue childhood. if you havent google the rules 
of this game and write a python program cpable of playing this game with the user.
'''
# made by:-Mr Domadiya Mittal
import random
print("          game name is 'snake water gun'")
print("'1' is for snake , '2' is for water , '3' for gun")
def game(compp,youu):
    if compp==1 and youu==1:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-draw"
        d=b+a
        return d
    elif compp==1 and youu==2:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-you loss the game."
        d=b+a
        return d
    elif compp==1 and youu==3:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-you win the game."
        d=b+a
        return d
    elif compp==2 and youu==1:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-you win the game."
        d=b+a
        return d
    elif compp==2 and youu==2:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-draw."
        d=b+a
        return d
    elif compp==2 and youu==3:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-you loss the game."
        d=b+a
        return d
    elif compp==3 and youu==1:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-you loss the game."
        d=b+a
        return d
    elif compp==3 and youu==2:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-you win the game."
        d=b+a
        return d
    elif compp==3 and youu==3:
        b=str("computer has enter ")+str(compp)+str("\nyou entered ")+str(youu)+("\n")
        a=" result:-draw."
        d=b+a
        return d
    else:
        a="you enterd wrong choise you can enter only frome 1 , 2 , 3 number"
        return a
comp=random.randint(1,3)
you=int(input("to choose snake press(1) or water press(2) or gun press(3)"))
c=game(comp,you)
print(game(comp,you))
