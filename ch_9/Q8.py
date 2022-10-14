with open("thia.txt") as f:
    file=f.read()
with open("that.txt",'w') as g:
    g.write(file)