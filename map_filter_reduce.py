import math
import statistics
from functools import reduce

def area(r):
    """Area of a circle with radius 'r'"""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# one way to do this

areas = []
for r  in radii:
    a = area(r)
    areas.append(a)

# using map

# output is a map object
map(area, radii)

#output is a list
list(map(area, radii))

temps = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19),
        ('Los Angeles', 26), ('Tokyo', 27), ('New York', 28),
        ('London', 22), ('Beijing', 32)]

c_to_f = lambda data: (data[0], (9/5*data[1] + 32))

list(map(c_to_f, temps))

# Filter

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = statistics.mean(data)
print(avg)

# returns a filter object
filter(lambda x: x > avg, data)

# returns a list
list(filter(lambda x: x > avg, data))
print(list(filter(lambda x: x > avg, data)))

# Remove missing data
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Columbia",
            "", "Ecuador", "", "", "Venezuela"]

print(list(filter(None, countries)))

# reduce Function

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

multiplier = lambda x, y: x*y
print(reduce(multiplier, prime_numbers))

product = 1
for x in prime_numbers:
    product *= x
print(product)
