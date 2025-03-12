# Using `yield from` in Coroutines

In this step, we'll explore how to use the `yield from` statement with coroutines for more practical applications. Coroutines are a powerful concept in Python, and understanding how to use `yield from` with them can greatly simplify your code.

## Coroutines and Message Passing

Coroutines are special functions that can receive values through the `yield` statement. They're incredibly useful for tasks such as data processing and event handling. In the `cofollow.py` file, there's a `consumer` decorator. This decorator helps set up coroutines by automatically advancing them to the first `yield` point. This means you don't have to manually start the coroutine; the decorator takes care of it for you.

Let's create a coroutine that receives values and validates their types. Here's how you can do it:

1. First, open the `cofollow.py` file in the editor. You can use the following command in the terminal to navigate to the correct directory:

```bash
cd /home/labex/project
```

2. Next, add the following `receive` function at the end of the `cofollow.py` file. This function is a coroutine that will receive a message and validate its type.

```python
def receive(expected_type):
    """
    A coroutine that receives a message and validates its type.
    Returns the received message if it matches the expected type.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

Here's what this function does:

- It uses `yield` without an expression to receive a value. When the coroutine is sent a value, this `yield` statement will capture it.
- It checks if the received value is of the expected type using the `isinstance` function. If the type doesn't match, it raises an `AssertionError`.
- If the type check passes, it returns the value.

3. Now, let's create a coroutine that uses `yield from` with our `receive` function. This new coroutine will receive and print integers only.

```python
@consumer
def print_ints():
    """
    A coroutine that receives and prints integers only.
    Uses yield from to delegate to the receive coroutine.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. To test this coroutine, open a Python shell and run the following code:

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

You should see the following output:

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## Understanding How `yield from` Works with Coroutines

When we use `yield from receive(int)` in the `print_ints` coroutine, the following steps occur:

1. Control is delegated to the `receive` coroutine. This means that the `print_ints` coroutine pauses, and the `receive` coroutine starts executing.
2. The `receive` coroutine uses `yield` to receive a value. It waits for a value to be sent to it.
3. When a value is sent to `print_ints`, it's actually received by `receive`. The `yield from` statement takes care of passing the value from `print_ints` to `receive`.
4. The `receive` coroutine validates the type of the received value. If the type is correct, it returns the value.
5. The returned value becomes the result of the `yield from` expression in the `print_ints` coroutine. This means that the `val` variable in `print_ints` gets assigned the value returned by `receive`.

Using `yield from` makes the code more readable than if we had to handle the yielding and receiving directly. It abstracts away the complexity of passing values between coroutines.

## Creating More Advanced Type-Checking Coroutines

Let's expand our utility functions to handle more complex type validation. Here's how you can do it:

1. Add the following functions to the `cofollow.py` file:

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. To test the new coroutine, open a Python shell and run the following code:

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

You should see output like this:

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

The `yield from` statement makes the code cleaner and more readable. It allows us to focus on the high-level logic of our program rather than getting bogged down in the details of message passing between coroutines.
