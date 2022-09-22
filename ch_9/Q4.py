'''
a file contains a words "donkey" multiple times. you need to write a program which replace this word with ###### by updating the same file.
'''

with open("donkey.txt",'r') as f:
    read=f.read()
    read=read.replace("donkey","######")
with open("donkey.txt",'w') as f:
    f.write(read)