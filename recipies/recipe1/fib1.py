"""
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.

    The 2 is found by adding the two numbers before it (1+1)
    Similarly, the 3 is found by adding the two numbers before it (1+2),
    And the 5 is (2+3),
    and so on!

"""

"""
Using lists to return a list of fib numbers
"""


def fib1(limit=10):
    """
    Returns a list of fib numbers
    """    
    nth_number = limit
    
    if limit <= 2:
        answer = [0]

    elif limit == 2:
        answer = [0,1]

    else:
        fib_num = [0,1]
        
        while len(fib_num) < nth_number:
            fib1 = fib_num[len(fib_num)-2]
            fib2 = fib_num[len(fib_num)-1]
            fib3 = fib2 + fib1
            fib_num.append(fib3)

        answer = fib_num

    return fib_num


"""
How to return a specific fib number.
"""

def fib2(nth_num=10):
    """
    Returns the nth fib number
    """

    # Base cases
    fib1 = 0
    fib2 = 1

    if nth_num <= 1:
        answer = fib1

    elif nth_num == 2:
        answer = fib2

    else:
        current_fib = 2

        while nth_num - current_fib > 0:
            fib1, fib2 = fib2, fib1 + fib2
            current_fib = current_fib + 1

        answer = fib2

    return fib2

if __name__ == "__main__":
    print(fib1(10))
    print(fib2(10))
     
