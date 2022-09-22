''' write a program to read the text frome a given file 'poems.txt'
 and find out whether it contains the words twinkle.'''
f=open('poems.txt','r')
b=f.read()
if 'twinkle' in b:
    print("twinkle is present in the poem.")
else:
    print("twinkle is not present in the poem.")