from math import sqrt

a = 5
print('Длинна первого катета = ',a)
b = 7
print('Длинна второго катета = ', b)

gg = (a * a) + (b * b)
g = sqrt(gg)

s = 0.5 * (a + b + g)

print('Длинна гипотенузы = ', g)
print('Площадь треугольника = ', s)