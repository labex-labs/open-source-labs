# Compose Functions

## Introduction

Function composition is a technique used in functional programming to combine two or more functions to form a new function. In Python, we can use the `functools.reduce()` function to perform right-to-left function composition.

## Problem

Write a function called `compose(*fns)` that accepts one or more functions as arguments and returns a new function that is the result of composing the input functions from right to left. The last (rightmost) function can accept one or more arguments; the remaining functions must be unary.

## Example

```py
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```

In the example above, we define two functions `add5` and `multiply`. We then use the `compose()` function to create a new function called `multiply_and_add_5` that first multiplies its two arguments and then adds 5 to the result. When we call `multiply_and_add_5(5, 2)`, we get the result `15`.

## Summary

In this challenge, you learned how to use the `functools.reduce()` function to perform right-to-left function composition in Python. You also wrote a function called `compose()` that accepts one or more functions as arguments and returns a new function that is the result of composing the input functions from right to left.
