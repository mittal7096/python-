# creat a class with a class attribute 'a';
# create an object frome it and set a directly using object a=0. does this change the class attribute?

class semple:
    a='mittal'
obj=semple()
obj.a='krishna'
print(semple.a)
print(obj.a)
