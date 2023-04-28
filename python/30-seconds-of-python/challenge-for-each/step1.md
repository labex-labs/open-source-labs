# Execute Function for Each List Element

## Problem

Write a function `for_each(itr, fn)` that takes a list `itr` and a function `fn` as arguments. The function should execute `fn` once for each element in `itr`.

## Example

```py
def print_square(num):
    print(num*num)

for_each([1, 2, 3], print_square) # prints 1 4 9
```

In the example above, the `for_each` function is called with a list `[1, 2, 3]` and a function `print_square`. The `print_square` function is executed once for each element in the list, printing the square of each number.
