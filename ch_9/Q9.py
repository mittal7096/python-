old='that.txt'
with open(old) as f:
    file=f.read()
with open('thia.txt') as g:
    file1=g.read()
if file==file1:
    print('a file is identical and both files are same.')
else:
    print('a file is not identical and both files are not same.')