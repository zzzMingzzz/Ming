def polynomial(*args):
    a = args[::-1]

    def calculate(x):
        total = 0
        for i in range(1, len(a)):
            total += a[i]*(x**i)
            return total

    return calculate()   ####????????
       

print(polynomial(0, 2))
