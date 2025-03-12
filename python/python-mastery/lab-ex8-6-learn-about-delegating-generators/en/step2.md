# Using `yield from` in Coroutines

In this step, you will learn how to use `yield from` with coroutines for more practical applications.

## Coroutines and Message Passing

Coroutines are functions that can receive values through the `yield` statement. They are useful for tasks like data processing and event handling. The `consumer` decorator in `cofollow.py` helps set up coroutines by automatically advancing them to the first `yield` point.

Let's create a coroutine that receives values and validates their types:

1. Open the `cofollow.py` file in the editor:

```bash
cd /home/labex/project
```

2. Add the following `receive` function at the end of the file:

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

This function:

- Uses `yield` without an expression to receive a value
- Checks if the received value is of the expected type
- Returns the value if it passes the type check

3. Now, let's create a coroutine that uses `yield from` with our `receive` function:

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

4. Test the coroutine in a Python shell:

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

When we use `yield from receive(int)` in the `print_ints` coroutine:

1. Control is delegated to the `receive` coroutine
2. The `receive` coroutine yields to receive a value
3. When a value is sent to `print_ints`, it's actually received by `receive`
4. The `receive` coroutine validates the type and returns the value
5. The returned value becomes the result of the `yield from` expression

This makes the code more readable than if we had to handle the yielding and receiving directly.

## Creating More Advanced Type-Checking Coroutines

Let's expand our utility functions to handle more complex type validation:

1. Add the following functions to `cofollow.py`:

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

2. Test the new coroutine in a Python shell:

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

You should see output like:

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

The `yield from` statement makes the code cleaner and more readable, allowing us to focus on the high-level logic rather than the details of message passing.
