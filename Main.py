import math

a = 0
b = 1
x1 = -1/math.sqrt(3)
x2 = 1/math.sqrt(3)


def testFunc(x):
    return math.log(1+x**2)


def derivTestFunc(x):
    return (2*x)/(1+x**2)


def leftSum(n, h, func):
    return sum([func(a + i*h) for i in range(n-1)]) * h


def metEiler(n, h, func, deriv):
    return ((h/2)*(func(a) + func(b)) +
            h*sum([func(a + i*h) for i in range(n-1)]) +
            (h**2)/12*(deriv(a)-deriv(b)))


def calcError(sumHalfH, sumH, p):
    return (sumHalfH - sumH)/(2**p - 1)


def metGauss(func, c, d, parts_count):
    parts = range(parts_count-1)
    def substVar(x, i, parts_count):
        return 1/(parts_count*2) * x + 1/(parts_count*2) * (2 * i + 1)
    return 1/(len(parts)*2) * sum([func(substVar(c, i, len(parts))) + func(substVar(d, i, len(parts))) for i in parts])


print('Приближенное значение по методу левых прямоугольников ')

params = [(10, 0.1), (20, 0.05), (40, 0.025)]
prev_value = None
for (n, h) in params :
    current_value = leftSum(n, h, testFunc)
    print('с шагом {h} = {result}'.format(h=h, result=current_value))
    if prev_value :
        error_size = calcError(current_value, prev_value, 1)
        print('погрешность для шага {h} = {error_size}'.format(error_size=error_size, h=h))
    prev_value = current_value

print('Приближенное значение по методу Эйлера ')

prev_value = None
for (n, h) in params :
    current_value = metEiler(n, h, testFunc, derivTestFunc)
    print('с шагом {h} = {result}'.format(h=h, result=current_value))
    if prev_value :
        error_size = calcError(current_value, prev_value, 1)
        print('погрешность для шага {h} = {error_size}'.format(error_size=error_size, h=h))
    prev_value = current_value

print('Метод Гаусса: {result}'.format(result=metGauss(testFunc, x1, x2, 4)))
