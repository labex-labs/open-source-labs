# Closures as a Data Structure

Closures provide a powerful mechanism for data encapsulation in Python. They allow you to create functions that maintain and manipulate private data without using classes or global variables.

Let's create a file called `counter.py` to demonstrate this concept:

1. Open the WebIDE and create a new file named `counter.py` in the `/home/labex/project` directory.

2. Add the following code to the file:

```python
def counter(value):
    """
    Create a counter with increment and decrement functions.

    Args:
        value: Initial value of the counter

    Returns:
        Two functions: one to increment the counter, one to decrement it
    """
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

This code defines a function `counter()` that creates two inner functions that share access to the same `value` variable. The `nonlocal` keyword allows the inner functions to modify the `value` variable from the enclosing scope.

3. Now let's create a test file to see this in action. Create a new file named `test_counter.py` with the following content:

```python
from counter import counter

# Create a counter starting at 0
up, down = counter(0)

# Increment the counter several times
print("Incrementing the counter:")
print(up())  # Should print 1
print(up())  # Should print 2
print(up())  # Should print 3

# Decrement the counter
print("\nDecrementing the counter:")
print(down())  # Should print 2
print(down())  # Should print 1
```

4. Run the test file by executing the following command in the terminal:

```bash
python3 test_counter.py
```

You should see the following output:

```
Incrementing the counter:
1
2
3

Decrementing the counter:
2
1
```

Notice how there is no class definition involved here. The `up()` and `down()` functions are manipulating a shared value that is neither a global variable nor an instance attribute. This value is stored in the closure, making it accessible only to the functions returned by `counter()`.

This is an example of how closures can be used as a data structure. The enclosed variable `value` is maintained between function calls, and it's private to the functions that access it.
