import math

def area(r):
    """Area of a circle with radius 'r'"""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# one way to do this

areas = []
for r  in radaii:
    a = area(r)
    areas.appemnd(a)

# using map

# output is a map object
map(area, radaii)

#output is a list
list(map(area, radaii))

temps = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19),
        ('Los Angeles', 26), ('Tokyo', 27), ('New York', 28),
        ('London', 22), ('Beijing', 32)]

c_to_f = lambda data: (data[0], (9/5*data[1] + 32))

list(map(c_to_f, temps))
