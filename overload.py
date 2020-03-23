# 2020, 1/14, by Queenie

# it matters with inheritance for passing object into father class thru param
# a method can be instantiate by many classes.
# python engine will determine to call which methods (overload) using dynamic binding.

class Cat:

    def__string__(self):
        return "Cat ! Miao ~"

    def printCat(self):
        print(self.__string__())

class Tiger(Cat):
    def__string__(self):
        return "Tiger is Cat, but Cat is not Tiger."

c = Cat()
t = Tiger()
c.printCat()
t.printCat()

    
