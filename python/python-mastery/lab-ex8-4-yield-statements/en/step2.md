# Handling Exceptions in Generators

In this step, you will learn how to handle exceptions in generators and coroutines using the `throw()` method.

## Understanding Coroutines

A coroutine is a specialized type of generator that can both consume values (through the `send()` method) and yield values. The `cofollow.py` file contains a simple coroutine implementation.

Open the `cofollow.py` file in the WebIDE editor:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
```

In this code:

- The `consumer` decorator automatically advances the generator to its first `yield` statement, making it ready to receive values.
- The `printer()` coroutine receives values via `yield` and prints them.

## Adding Exception Handling to the Coroutine

Now, let's modify the `printer()` coroutine to handle exceptions. Update the `printer()` function in `cofollow.py` as follows:

```python
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

Save the file after making these changes.

## Experimenting with Exception Handling in Coroutines

Let's experiment with throwing exceptions into the coroutine. Open a terminal and run the Python interpreter:

```bash
cd ~/project
python3
```

### Experiment 1: Basic Coroutine Usage

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')  # Send a value to the coroutine
hello
>>> p.send(42)  # Send another value
42
```

The coroutine processes the values we send to it without issues.

### Experiment 2: Throwing an Exception into the Coroutine

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

When we throw an exception into the coroutine using the `throw()` method, it is caught by our try-except block and handled gracefully.

### Experiment 3: Throwing a Real Exception into the Coroutine

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

Here, we're catching a real exception from a failed operation and then throwing that exception into our coroutine, which handles it as expected.

### Experiment 4: Verifying the Coroutine Continues Running

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

Notice that even after handling exceptions, the coroutine is still active and can continue to process values.

## Key Takeaways

1. Generators and coroutines can handle exceptions at the point of the `yield` statement.
2. The `throw()` method allows you to inject exceptions into a generator or coroutine.
3. Properly handling exceptions in generators lets you create robust, error-tolerant generators that can continue running even when errors occur.

Exit the Python interpreter by typing `exit()` or pressing `Ctrl+D`.
