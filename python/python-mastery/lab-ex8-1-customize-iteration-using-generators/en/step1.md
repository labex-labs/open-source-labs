# Understanding Python Generators

Generators are a powerful feature in Python. They offer a simple and elegant way to create iterators. In Python, when you deal with data sequences, iterators are very useful as they allow you to loop through a series of values one by one. Regular functions typically return a single value and then stop executing. However, generators are different. They can yield a sequence of values over time, which means they can produce multiple values in a step - by - step manner.

## What is a Generator?

A generator function has a similar appearance to a regular function. But the key difference lies in how it returns values. Instead of using the `return` statement to provide a single result, a generator function uses the `yield` statement. The `yield` statement is special. Each time it is executed, the function's state is paused, and the value that follows the `yield` keyword is returned to the caller. When the generator function is called again, it resumes execution right where it left off.

Let's start by creating a simple generator function. The built - in `range()` function in Python doesn't support fractional steps. So, we'll create a generator function that can produce a range of numbers with a fractional step.

1. First, you need to open a new Python terminal in the WebIDE. To do this, click on the "Terminal" menu and then select "New Terminal".
2. Once the terminal is open, type the following code in the terminal. This code defines a generator function and then tests it.

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

In this code, the `frange` function is a generator function. It initializes a variable `current` with the `start` value. Then, as long as `current` is less than the `stop` value, it yields the `current` value and then increments `current` by the `step` value. The `for` loop then iterates over the values produced by the `frange` generator function and prints them.

You should see the following output:

```
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

## The One - Time Nature of Generators

An important characteristic of generators is that they are exhaustible. This means that once you have iterated through all the values produced by a generator, it can't be used again to produce the same sequence of values. Let's demonstrate this with the following code:

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

In this code, we first create a generator object `f` using the `frange` function. The first `for` loop iterates over all the values produced by the generator and prints them. After the first iteration, the generator has been exhausted, which means it has already produced all the values it can. So, when we try to iterate over it again in the second `for` loop, it doesn't produce any new values.

Output:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:

```

Notice that the second iteration didn't produce any output because the generator was already exhausted.

## Creating Reusable Generators with Classes

If you need to iterate multiple times over the same sequence of values, you can wrap the generator in a class. By doing this, each time you start a new iteration, a fresh generator will be created.

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

In this code, we define a class `FRange`. The `__init__` method initializes the `start`, `stop`, and `step` values. The `__iter__` method is a special method in Python classes. It is used to create an iterator. Inside the `__iter__` method, we have a generator that produces values in a similar way to the `frange` function we defined earlier.

When we create an instance `f` of the `FRange` class and iterate over it multiple times, each iteration calls the `__iter__` method, which creates a fresh generator. So, we can get the same sequence of values multiple times.

Output:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

This time, we can iterate multiple times because the `__iter__()` method creates a fresh generator each time it's called.
