from functools import lru_cache

def check_proper_data_type(number):
    if type(number) == int:
        if number > 0:
            return False
        else:
            return 'choose a number greater than 0'
    else:
        return 'choose a whole number'


def matts_fibonacci(number):
    """returns the nth element in the fibonacci sequence"""
    if number == 1 or number == 2:
        return 1
    else:
        sequence = [1,1]
        number -= 1
        for x in range(number):
            sequence.append(sequence[-2]+sequence[-1])
        return sequence[-1]

# Slow fibonacci function
def fibonacci_slow(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# Fibonacci function using a dictionary for cashing values
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

# Fibonacci function using lru_cache
@lru_cache(maxsize = 1000)
def fibonacci_lru_cache(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_lru_cache(n-1) + fibonacci_lru_cache(n-2)

# test
def test(n,function):
    if check_proper_data_type(n) == False:
        if function == "lru":
            for x in range(1,n+1):
                print(x, ":", fibonacci_lru_cache(x))
        elif function == "matt":
            for x in range(1,n+1):
                print(x, ":", matts_fibonacci(x))
        elif function == "simple cash":
            for x in range(1,n+1):
                print(x, ":", cash_fibonacci(x))
        elif function == "slow":
            for x in range(1,n+1):
                print(x, ":", fibonacci_slow(x))
        else:
            print("not an available function choice")

test(1000, "matt")
