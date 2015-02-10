import doctest

def fib1(n):
    """Return n-th Fibonacci number.

    Example:
    >>> fib1(1)
    1
    >>> fib1(2)
    1
    >>> fib1(6)
    8

    Implementation detail: this function
    uses recursion
    """
    if n <= 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)

def fib2(n):
    """Return n-th Fibonacci number.

    Example:
    >>> fib2(1)
    1
    >>> fib2(2)
    1
    >>> fib2(6)
    8

    Implementation detail: this function
    works in linear time.
    """
    a = b = 1
    for x in range(n - 2):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    print(doctest.testmod())
