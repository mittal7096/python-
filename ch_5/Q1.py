words={"gyan":"knowlage",
       "pustak":"book",
       "chokaro":"boy",
       "chokare":"girl",
       "varsad":"rain",
       "havaa":"air"}
print(words.keys())
a=input("enter word frome the above list with you want to translet:- ")
print('trensletion of ',a,'is:-',words.get(a))