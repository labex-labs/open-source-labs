# Creating a Task Scheduler with Generators

Now let's build a simple task scheduler that can run multiple generator functions concurrently. This demonstrates how generators can be managed to perform cooperative multitasking.

Create a new file called `multitask.py` in the `/home/labex/project` directory:

```python
# multitask.py

from collections import deque

# Task queue
tasks = deque()

# Simple task scheduler
def run():
    while tasks:
        task = tasks.popleft()  # Get the next task
        try:
            task.send(None)     # Resume the task
            tasks.append(task)  # Put it back in the queue
        except StopIteration:
            print('Task done')  # Task is complete

# Example task 1: Countdown
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield              # Pause execution
        n -= 1

# Example task 2: Count up
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield              # Pause execution
        x += 1
```

Let's understand how this task scheduler works:

1. We use a `deque` (double-ended queue) to store our generator tasks.
2. The `run()` function takes tasks from the queue one by one:
   - It resumes each task using `send(None)` (similar to `next()`)
   - After the task yields, it's added back to the end of the queue
   - When a task completes (raises `StopIteration`), it's removed
3. Each `yield` statement in our generator tasks acts as a pause point, allowing other tasks to run

This approach implements cooperative multitasking - each task voluntarily yields control back to the scheduler, allowing other tasks to run.
