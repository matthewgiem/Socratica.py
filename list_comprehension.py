squares = []
for i in range(1, 101):
    squares.append(i**2)

squares2 = [i**2 for i in range(1,101)]

remainders5 = [x**2 % 5 for x in range(1,101)]

remainders11 = [x**2 % 11 for x in range(1, 101)]

p_remainders = [x**2 % p for x in range(0,p)] # Gauss Quadriatic Reciprocity

#len(p_remainders) = (p + 1)/2

movies = ["list of movies"]

gmovies = [title for title in movies if title.startswith("G")]

movies = [('movie title', year),...]

released_before_2000 = [title for (title, year) in movies if year < 2000]

# list comprehension for vector multiplication

v = [2, -3, 1]

v_times_4 = [4*x for x in v]

# Cartesian Product

A = [1,3,5,7]
B = [2,4,6,8]

cartesian_product = [(a,b) for a in A for b in B]
