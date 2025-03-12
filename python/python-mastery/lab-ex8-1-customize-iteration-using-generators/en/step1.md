# Understanding Python Generators

Generators are a powerful feature in Python that allow you to create iterators in a simple and elegant way. Unlike regular functions that return a value and then terminate, generators yield a sequence of values over time.

## What is a Generator?

A generator function looks like a regular function but instead of using `return` to provide a result, it uses the `yield` statement to produce a series of values. Each time the `yield` statement is executed, the function's state is paused and the yielded value is returned to the caller. When the generator function is called again, execution resumes where it left off.

Let's start by creating a simple generator function that produces a range of numbers with a fractional step (which is not supported by the built-in `range()` function):

1. Open a new Python terminal in the WebIDE by clicking on the "Terminal" menu and selecting "New Terminal"

2. Type the following code in the terminal to define and test a generator function:

```python
def frange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

# Test the generator with a for loop
for x in frange(0, 2, 0.25):
    print(x, end=' ')
```

You should see the following output:

```
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

## The One-Time Nature of Generators

An important characteristic of generators is that they're exhaustible - once you iterate through a generator, it's consumed and can't be reused. Let's demonstrate this:

```python
# Create a generator object
f = frange(0, 2, 0.25)

# First iteration works fine
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

# Second iteration produces nothing
print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

Output:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:

```

Notice that the second iteration didn't produce any output because the generator was already exhausted.

## Creating Reusable Generators with Classes

If you need to iterate multiple times over the same sequence, you can wrap the generator in a class:

```python
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step

# Create an instance
f = FRange(0, 2, 0.25)

# We can iterate multiple times
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

Output:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

This time, we can iterate multiple times because the `__iter__()` method creates a fresh generator each time it's called.
