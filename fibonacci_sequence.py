from functools import lru_cache

def matts_fibonacci(number):
    """returns the nth element in the fibonacci sequence"""
    if type(number) == int:
        if number > 0:
            if number == 1 or number == 2:
                return 1
            else:
                sequence = [1,1]
                number -= 1
                for x in range(number):
                    sequence.append(sequence[-2]+sequence[-1])
                return sequence[-1]
        else:
            print('choose a number greater than 0')
    else:
        print('choose a whole number')

def fibonacci_slow(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_slow(n-1) + fibonacci_slow(n-2)

fibonacci_cash = {}
def cash_fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cash:
        return fibonacci_cash[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = cash_fibonacci(n - 1) + cash_fibonacci(n - 2)

    # Cache the value and return it
    fibonacci_cash[n] = value
    return value

@lru_cache(maxsize = 1000)
def fibonacci_lru_cache(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_lru_cache(n-1) + fibonacci_lru_cache(n-2)

# test
for n in range(1,1001):
    print(n, ":", fibonacci_lru_cache(n))
