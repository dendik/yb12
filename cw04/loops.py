##for x in ["a", 2, "hello"]:
##    print(x)
##
##for x in range(10):
##    print(x)
##
##import itertools
##for x in itertools.count(1):
##    print(x)

def fib1(n):
    """Return n-th Fibonacci number.

    Example:
    >>> fib1(1)
    1
    >>> fib1(2)
    1
    >>> fib1(6)
    8
    """
    if n <= 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)

print(__name__)
