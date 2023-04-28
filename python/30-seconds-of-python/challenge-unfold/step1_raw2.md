# Unfold List

## Introduction

In Python, we can create a list using a variety of methods. One such method is by using an iterator function and an initial seed value. In this challenge, you will be tasked with building a list using an iterator function and an initial seed value.

## Problem

Your task is to implement the `unfold` function that takes an iterator function and an initial seed value as arguments. The iterator function accepts one argument (`seed`) and must always return a list with two elements ([`value`, `nextSeed`]) or `False` to terminate. The `unfold` function should use a generator function, `fn_generator`, that uses a `while` loop to call the iterator function and `yield` the `value` until it returns `False`. Finally, the `unfold` function should use a list comprehension to return the list that is produced by the generator, using the iterator function.

Implement the `unfold` function:

```python
def unfold(fn, seed):
    # your code here
```

### Input

- An iterator function `fn` that accepts one argument (`seed`) and must always return a list with two elements ([`value`, `nextSeed`]) or `False` to terminate.
- An initial seed value `seed`.

### Output

- A list that is produced by the generator, using the iterator function.

### Example

```python
f = lambda n: False if n > 50 else [-n, n + 10]
assert unfold(f, 10) == [-10, -20, -30, -40, -50]
```

## Summary

In this challenge, you have learned how to build a list using an iterator function and an initial seed value. You have implemented the `unfold` function that takes an iterator function and an initial seed value as arguments and returns a list that is produced by the generator, using the iterator function.
