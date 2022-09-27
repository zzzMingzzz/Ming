class polynomial():
    def __init__(self, *args):
        self.args = args[::-1]
        
    def x_values(self, x):
        total = 0
        for i in range(1, len(self.args)):
            total += self.args[i]*(x**i)
        return total


p = polynomial(3, 3, 3, 4)
print(p.x_values(-7))
