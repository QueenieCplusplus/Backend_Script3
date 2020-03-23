# 2020, 1/14, AM 10:15, by Queenie Chen
# override

class A:

    def__init__(self, i=0):
        self.i=i

    def mmm(self):
        self.i *= 100

class B(A):
    def__init__(self, j=0):
        super().__init__(6)
        self.j = j 

    def mmm(self):
        self.i *= 1000

def main():
    a = A()
    b = B()
    a.mmm(9)
    b.mmm()
    print(b.i)
    print(b.j)

main()

    