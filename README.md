<h1 align="center">Python scripts</h1>
<div align="center">

![Python version](https://img.shields.io/badge/python-3.7+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

This is a collection of short Python scripts I use as utility tools or just for testing of various features.

### [compare_memory_usage_lst_comp_v_gen.py](https://github.com/adamsqi/python-scripts/blob/master/compare_memory_usage_lst_comp_v_gen.py)


+ Author: [Kamil Adamski](https://github.com/adamsqi)

+ Created at: 2020.06.21

#### Description: 
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





