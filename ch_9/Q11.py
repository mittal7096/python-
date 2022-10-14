import os
with open('Q11.txt') as f:
    read=f.read()
with open('rename_by_python.txt','w') as g:
    g.write(read)
os.remove('Q11.txt')