# Understanding Coroutines with a File Follower

Let's start by understanding what coroutines are and how they work in Python. A coroutine is a specialized version of a generator function that can both consume and produce data. Unlike regular functions that start from the beginning every time they're called, coroutines can suspend and resume their execution.

## Creating a Basic Coroutine File Follower

In this step, we'll create a file follower that uses coroutines to monitor a file for new content and process it. This is similar to the Unix `tail -f` command.

1. Open the code editor and create a new file named `cofollow.py` in the `/home/labex/project` directory.

2. Copy the following code into the file:

```python
# cofollow.py
import os
import time

# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = f.readline()
            if line != '':
                target.send(line)  # Send the line to the target coroutine
            else:
                time.sleep(0.1)  # Sleep briefly if no new content

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)  # Prime the coroutine (necessary first step)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('stocklog.csv', printer())
```

3. Let's understand the key components of this code:

   - `follow(filename, target)`: This function opens a file and continuously reads new lines, sending each line to a target coroutine.
   - `@consumer` decorator: This decorator helps initialize coroutines by automatically "priming" them (sending the initial `None` value).
   - `printer()` coroutine: A simple coroutine that receives values and prints them.

4. Save the file and run it from the terminal:

```bash
cd /home/labex/project
python3 cofollow.py
```

5. You should see the script printing the content of the stock log file, and it will continue to print new lines as they are added to the file. Press `Ctrl+C` to stop the program.

The key concept here is that data flows from the `follow` function into the `printer` coroutine through the `send` method. This "pushing" of data is opposite to generators, which "pull" data through iteration.
