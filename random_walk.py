import random
import operator

direction = [(0,1), (1,0), (-1,0), (0,-1)]

def random_walk(n):
    start = (0,0)
    for _ in range(n):
        start = tuple(map(operator.add, start, random.choice(direction)))
    x, y = start
    return abs(x) + abs(y)


answer = {}
for x in range(11,15):
    throw_away = 0
    for y in range(1000000):
        throw_away += random_walk(x)
    answer[x] = throw_away/1000000


print(answer)


# for 1000000 times values are the following
# {11: 3.701996, 12: 3.867038, 13: 4.02745, 14: 4.18464}
# {11: 3.699582, 12: 3.866506, 13: 4.029168, 14: 4.183024}
