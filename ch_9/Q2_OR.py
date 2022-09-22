# write a game() function in a program lets a user play a game and return the score as an integer.
# you need to read a file 'hidcore.txt' which is either black or contains the previous hi=score whenever game() breaks the hi-score.

def game():
    return 344


score=game()
with open('hidcore.txt') as f:
    higscore=f.read()
if higscore<str(score):
    with open('hidcore.txt','w') as g:
        g.write(str(score))
elif higscore=="":
    with open('hidcore.txt', 'w') as g:
        g.write(str(score))
aa=open('hidcore.txt')
e=aa.read()
print(e)