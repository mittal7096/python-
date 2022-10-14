class country:
    country="india"
    def passpote(self):
        print("you are indian and you love india.")
class state:
    state="gujarat"
    def adharcad(self):
        print("you are gujarati and you live in india")
class address(country,state):
    city="motavaracha"
    def location(self):
        print("you are proper gujarati and your mother tong is gujarati")
a = address()
print(a.country)
print(a.state)
print(a.city)
a.passpote()
a.adharcad()
a.location()


    
    