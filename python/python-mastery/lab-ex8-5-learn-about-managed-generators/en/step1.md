# Understanding Python Generators

Let's start by reviewing what generators are in Python. Generators are a special type of function that returns an iterator which we can iterate through. Unlike regular functions, generators use the `yield` statement to return values one at a time, suspending their execution between yields.

## Creating a Simple Generator

In the WebIDE, create a new file called `generator_demo.py` in the `/home/labex/project` directory with the following content:

```python
# Generator function that counts down from n
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Countdown complete!")

# Create a generator object
counter = countdown(5)

# Drive the generator manually
print(next(counter))  # 5
print(next(counter))  # 4
print(next(counter))  # 3

# Iterate through remaining values
for value in counter:
    print(value)  # 2, 1
```

Run this code by executing the following command in the terminal:

```bash
python3 /home/labex/project/generator_demo.py
```

You should see this output:

```
Starting countdown from 5
5
4
3
2
1
Countdown complete!
```

Note how the generator function:

1. Starts execution when we first call `next(counter)`
2. Pauses at each `yield` statement
3. Continues from where it left off when we call `next()` again
4. Completes its execution after the last value is yielded

This ability to pause and resume execution is what makes generators powerful for tasks like task scheduling and asynchronous programming.
