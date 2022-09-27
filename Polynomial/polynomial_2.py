class polynomial():
    total = 0
    def __init__(self, *args):
        self.args = args[::-1]
        
    def __call__(self, x):
        for i in range(len(self.args)):
            self.total += self.args[i]*(x**i)
        return self.total


p = polynomial(3, 3, 3, 4)
print(p(-7))

