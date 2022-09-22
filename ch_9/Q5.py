words=["donkey","gadhado"]
with open('donkey.txt') as f:
    reads=f.read()
for word in words:
    reads=reads.replace(word,"####")
with open('donkey.txt','w') as g:
    g.write(reads)