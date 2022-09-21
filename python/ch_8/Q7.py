# write a python function to remove a given word from a given list and strape it at the same time.
def streep(string,name):
    newstr=string.replace(name,"")
    return newstr.strip()
this="        mittal is a good man           "
n=streep(this,"mittal")
print(n)