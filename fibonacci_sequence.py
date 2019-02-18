def fibonacci(number):
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
