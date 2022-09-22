# write a game() function in a program lets a user play a game and return the score as an integer.
# you need to read a file 'hidcore.txt' which is either black or contains the previous hi=score whenever game() breaks the hi-score.

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
if c=="computer has enter 1\nyou entered 3\n result:-you win the game." or c=="computer has enter 2\nyou entered 1\n result:-you win the game." or c=="computer has enter 3\nyou entered 2\n result:-you win the game." :
    f=open('hidcore.txt','a')
    f.write('1 point of yours\n')
    f.close()
elif c=="computer has enter 1\nyou entered 1\n result:-draw." or c=="computer has enter 2\nyou entered 2\n result:-draw." or c=="computer has enter 3\nyou entered 3\n result:-draw.":
    f = open('hidcore.txt', 'a')
    f.write('computer 1 point and you got 1 point\n')
    f.close()
else:
    f = open('hidcore.txt', 'a')
    f.write('1 point of computer\n')