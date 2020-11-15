class myClass:
    #konstruktor
    def __init__(self, val,val2,sum):
        self.val = val
        self.val2 = val2
        self.sum = sum

    #metoda
    def getVal(self):

        print(self.val)
        print(self.val2)
        print(self.sum)
        print(self.val + self.val2)
