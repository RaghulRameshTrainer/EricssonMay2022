class One():
    def m1(self):
        print("CHENNAI")

class TWO():
    def m1(self):
        print("BANGALORE")
o=One()
t=TWO()

for city in (o,t):
    city.m1()

