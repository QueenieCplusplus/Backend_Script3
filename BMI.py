# BMI, 2020, 1/08, by Queenie Chen

class BMI:

    def __init__(self, name = "poupou", weight = 3, height = 100):
        self.__name = name
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        bmi = self.__weight / self.__height
        return round(bmi)

    def getName(self):
        return self.__name

    def getStatus(self):
        bbb = self.getBMI()
        if bbb < 18.5:
            return "under weight"
        elif bbb < 25:
            return "normal"
        else:
            return "over weight"

def main():
    b = BMI("queen", 52, 172)
    print(b.getName())
    print(b.getStatus())


main()
