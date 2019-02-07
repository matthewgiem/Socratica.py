# Scalene triangle: All sides hjave different lemngths
# Isosceles triangle: Two sides have the same lemngth
# Equilateral triangle: All sides are equal.

a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

# test for "real" triangle leg values and make user no value errors exist

if a != b and b != c and a != c:
    print("This is an Scalene triangle.")
elif a == b and b == c:
    print("This is an Equilateral triangle.")
else:
    print("This is an Isosceles triangle.")
