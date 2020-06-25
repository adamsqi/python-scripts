__author__ = '[Kamil Adamski](https://github.com/adamsqi)'
__date__ = '2020.06.21'

"""
This module shows a difference in memory usage
between using list comprehension and generators.
The results clearly show that list comprehensions
have excessive memory usage unlike generators.
The latter use a strictly defined storage space, 
regardless of the length of iterable. In addition, 
the computing time for using iterable is much less 
than list comprehensions.

Results:
```
total time execution time of function generate_suqares_using_list_comprehensions: 7.9959259033203125
get size of function generate_suqares_using_list_comprehensions results 859724472
total time execution time of function generate_suqares_using_generators: 0.0
get size of function generate_suqares_using_generators results 120
```
"""

import functools
import time
import sys

from typing import List

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        total_time = stop - start
        print(f'total time execution time of function {func.__name__}: {total_time}')
        print(f'get size of function {func.__name__} results {sys.getsizeof(result)}')
        return result
    return wrapper
    
def main():
    arbitrary_number = 10**8
    timeit(generate_suqares_using_list_comprehensions)(arbitrary_number)
    timeit(generate_suqares_using_generators)(arbitrary_number)
    
def calculate_square(number: int):
    """
    >>> number = 2
    >>> calculate_square(number)
    4
    """
    return number ** 2
    
def generate_suqares_using_list_comprehensions(number: int) -> List[int]:
    """
    >>> number = 5
    >>> generate_suqares_using_list_comprehensions(number)
    [0, 1, 2, 3, 4]
    """
    return [x for x in range(number)]

def generate_suqares_using_generators(number: int) -> List[int]:
    """
    >>> number = 5
    >>> generate_suqares_using_generators(number)
    <generator object generate_suqares_using_generators.<locals>.<genexpr> ...
    """
    return (x for x in range(number))
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
    main()
    