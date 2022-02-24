from Point import *
from Polynomial import *

#approximate y = 2^x
poly_one = Polynomial(Point(1, 2), Point(2, 4), Point(3, 8), Point(4, 16))

print('curve fit:', poly_one)

print('derivative:', poly_one.get_derivative())

print('indefinite integral:', poly_one.get_integral())

def_integral = poly_one.get_integral(C=0)
area = def_integral.evaluate(4) - def_integral.evaluate(-1)
print('area under the curve from -1 to 4:', area)

zeroes_in_range = poly_one.find_roots_range(-10, 10)
sol_str = 'x = '
for sol in zeroes_in_range:
    sol_str += str(sol) + ', '
sol_str = sol_str[:-2]
print('zeroes on (-10, 10):', sol_str)