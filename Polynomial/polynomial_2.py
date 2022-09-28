class polynomial():
    total = 0
    def __init__(self, *args):
        self.args = args[::-1]
        self.args1 = args
        
    def __call__(self, x):
        for i in range(len(self.args)):
            self.total += self.args[i]*(x**i)
        return self.total

    def __str__(self):
        polynomial_output = ""
        z = len(self.args1)
       
        for i in range(len(self.args1)):
            if z == 1:
                y = ""
            elif z == 2:
                y = "x"
            else:
                y = f"x^{z-1}"

            if i == 0:
                a = ""
            elif self.args1[i] > 0:
                a = "+"
            else:
                a = ""

            polynomial_output += f"{a}{self.args1[i]}{y}"
            z -= 1

        return polynomial_output
    


p = polynomial(-2, -4, 4)
print(p(1))
print(p)
