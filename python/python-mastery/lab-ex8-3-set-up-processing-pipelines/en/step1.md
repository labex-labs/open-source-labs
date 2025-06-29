# Understanding Coroutines with a File Follower

Let's start by understanding what coroutines are and how they work in Python. A coroutine is a specialized version of a generator function. In Python, functions usually start from the beginning every time they're called. But coroutines are different. They can both consume and produce data, and they have the ability to suspend and resume their execution. This means that a coroutine can pause its operation at a certain point and then pick up right where it left off later.

## Creating a Basic Coroutine File Follower

In this step, we'll create a file follower that uses coroutines to monitor a file for new content and process it. This is similar to the Unix `tail -f` command, which continuously shows the end of a file and updates as new lines are added.

1. Open the code editor and create a new file named `cofollow.py` in the `/home/labex/project` directory. This is where we'll write our Python code to implement the file follower using coroutines.

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
   - `follow(filename, target)`: This function is responsible for opening a file. It first moves the file pointer to the end of the file using `f.seek(0, os.SEEK_END)`. Then, it enters an infinite loop where it continuously tries to read new lines from the file. If a new line is found, it sends that line to the target coroutine using the `send` method. If there is no new content, it pauses for a short time (0.1 seconds) using `time.sleep(0.1)` before checking again.
   - `@consumer` decorator: In Python, coroutines need to be "primed" before they can start receiving data. This decorator takes care of that. It automatically sends an initial `None` value to the coroutine, which is a necessary first step to get the coroutine ready to receive real data.
   - `printer()` coroutine: This is a simple coroutine. It has an infinite loop where it uses the `yield` keyword to receive an item sent to it. Once it receives an item, it simply prints it.

4. Save the file and run it from the terminal:

```bash
cd /home/labex/project
python3 cofollow.py
```

5. You should see the script printing the content of the stock log file, and it will continue to print new lines as they are added to the file. Press `Ctrl+C` to stop the program.

The key concept here is that data flows from the `follow` function into the `printer` coroutine through the `send` method. This "pushing" of data is opposite to generators, which "pull" data through iteration. In a generator, you typically use a `for` loop to iterate over the values it produces. But in this coroutine example, the data is actively sent from one part of the code to another.
