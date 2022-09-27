class polynomial():
    def __init__(self, *args):
        self.args = args[::-1]
        
    def x_values(self, x):
        total = 0
        for i in range(1, len(self.args)):
            total += self.args[i]*(x**i)
        return total


p = polynomial(3, 3, 3, 4)
p.x_values(-7)


a = polynomial(2, 0)
a.x_values(0)