# Understanding the `yield from` Statement

In this step, you will learn about the `yield from` statement and how it can help with delegating generators.

## What is `yield from`?

The `yield from` statement was introduced in Python 3.3 to simplify the delegation of operations to subgenerators. It allows a generator to yield values from another generator directly, without having to use a loop.

Without `yield from`, if you wanted to delegate to another generator, you would need to write code like this:

```python
def delegating_generator():
    for value in subgenerator():
        yield value
```

With `yield from`, this becomes much simpler:

```python
def delegating_generator():
    yield from subgenerator()
```

This is not just syntactic sugar. `yield from` also handles the bidirectional communication between the caller and the subgenerator, passing values sent to the delegating generator through to the subgenerator.

## Basic Example

Let's create a simple example to illustrate how `yield from` works:

1. Open the `cofollow.py` file in the editor:

```bash
cd /home/labex/project
```

2. Add the following function at the end of the file:

```python
def subgen():
    for i in range(5):
        yield i

def main_gen():
    yield from subgen()
    yield 'Done'
```

3. Now, let's test these functions. Open a Python shell and run:

```python
from cofollow import subgen, main_gen

# Test subgen directly
for x in subgen():
    print(x)

# Test main_gen that delegates to subgen
for x in main_gen():
    print(x)
```

You should see the output:

```
0
1
2
3
4

0
1
2
3
4
Done
```

This demonstrates how `yield from` passes all values from `subgen()` through `main_gen()`.

## Value Passing with `yield from`

One powerful aspect of `yield from` is that it can handle value passing in both directions. Let's create a more complex example:

1. Add the following functions to `cofollow.py`:

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def caller():
    acc = accumulator()
    yield from acc
    yield 'Total accumulated'
```

2. Test these functions in a Python shell:

```python
from cofollow import caller

c = caller()
print(next(c))  # Start the coroutine
print(c.send(1))  # Send value 1, get accumulated value
print(c.send(2))  # Send value 2, get accumulated value
print(c.send(3))  # Send value 3, get accumulated value
print(c.send(None))  # Send None to exit the accumulator
```

You should see the output:

```
0
1
3
6
'Total accumulated'
```

This shows how `yield from` fully delegates all send/receive operations to the subgenerator until it's exhausted.

Now that you understand the basics of `yield from`, we'll move on to more practical applications in the next step.
