# Handling Exceptions in Generators

In this step, we're going to learn how to handle exceptions in generators and coroutines. But first, let's understand what exceptions are. An exception is an event that occurs during the execution of a program and disrupts the normal flow of the program's instructions. In Python, we can use the `throw()` method to handle exceptions in generators and coroutines.

## Understanding Coroutines

A coroutine is a special type of generator. Unlike regular generators that mainly yield values, coroutines can both consume values (using the `send()` method) and yield values. The `cofollow.py` file has a simple implementation of a coroutine.

Let's open the `cofollow.py` file in the WebIDE editor. Here's the code inside:

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

Now, let's break down this code. The `consumer` is a decorator. A decorator is a function that takes another function as an argument, adds some functionality to it, and then returns the modified function. In this case, the `consumer` decorator automatically moves the generator to its first `yield` statement. This is important because it makes the generator ready to receive values.

The `printer()` coroutine is defined with the `@consumer` decorator. Inside the `printer()` function, we have an infinite `while` loop. The `item = yield` statement is where the magic happens. It pauses the execution of the coroutine and waits to receive a value. When a value is sent to the coroutine, it resumes execution and prints the received value.

## Adding Exception Handling to the Coroutine

Now, we're going to modify the `printer()` coroutine to handle exceptions. We'll update the `printer()` function in `cofollow.py` like this:

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

The `try` block contains the code that might raise an exception. In our case, it's the code that receives and prints the value. If an exception occurs in the `try` block, the execution jumps to the `except` block. The `except` block catches the exception and prints an error message. After making these changes, save the file.

## Experimenting with Exception Handling in Coroutines

Let's start experimenting with throwing exceptions into the coroutine. Open a terminal and run the Python interpreter using the following commands:

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

Here, we first import the `printer` coroutine from the `cofollow` module. Then we create an instance of the `printer` coroutine named `p`. We use the `send()` method to send values to the coroutine. As you can see, the coroutine processes the values we send to it without any problems.

### Experiment 2: Throwing an Exception into the Coroutine

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

In this experiment, we use the `throw()` method to inject a `ValueError` exception into the coroutine. The `try-except` block in the `printer()` coroutine catches the exception and prints an error message. This shows that our exception handling is working as expected.

### Experiment 3: Throwing a Real Exception into the Coroutine

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

Here, we first try to convert the string `'n/a'` to an integer, which raises a `ValueError`. We catch this exception and then use the `throw()` method to pass it to the coroutine. The coroutine catches the exception and prints the error message.

### Experiment 4: Verifying the Coroutine Continues Running

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

After handling the exceptions, we send another value to the coroutine using the `send()` method. The coroutine is still active and can process the new value. This shows that our coroutine can continue running even after encountering errors.

## Key Takeaways

1. Generators and coroutines can handle exceptions at the point of the `yield` statement. This means that we can catch and handle errors that occur when the coroutine is waiting for or processing a value.
2. The `throw()` method allows you to inject exceptions into a generator or coroutine. This is useful for testing and for handling errors that occur outside the coroutine.
3. Properly handling exceptions in generators lets you create robust, error-tolerant generators that can continue running even when errors occur. This makes your code more reliable and easier to maintain.

To exit the Python interpreter, you can type `exit()` or press `Ctrl+D`.
