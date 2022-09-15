from cgi import print_directory


a={2,2,4,2,3,4,2,5,6,}
print(a)
# if we will try to creat the empty set then it will creat empty dict.
a={}
print(type(a))
# if we want to creat a empty set then we have to follow the given sintex.
b=set()
print(type(b))
# if we want to add value in set 
b.add(3)
print(b)
#we cannot add same value in the set .
b.add(3)
b.add(4)
b.add(5)
b.add(3)
b.add(8)
print(b)
# we canot add list or dictnory in the set

print(len(b))
b.remove(5)
print(b)
# if we use POP then it will remove value rendemly
b.pop()
print(b)