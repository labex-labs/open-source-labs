# Execute Function for Each List Element

## Introduction

In Python, it is common to need to execute a function for each element in a list. This can be done using a `for` loop, but it can be tedious to write out the loop every time. In this challenge, you will create a function that takes a list and a function as arguments and executes the function for each element in the list.

## Problem

Write a function `for_each(itr, fn)` that takes a list `itr` and a function `fn` as arguments. The function should execute `fn` once for each element in `itr`.

## Example

```py
def print_square(num):
    print(num*num)

for_each([1, 2, 3], print_square) # prints 1 4 9
```

In the example above, the `for_each` function is called with a list `[1, 2, 3]` and a function `print_square`. The `print_square` function is executed once for each element in the list, printing the square of each number.

## Summary

In this challenge, you created a function that takes a list and a function as arguments and executes the function for each element in the list. This is a useful technique for applying a function to every element in a list without having to write out a `for` loop every time.
