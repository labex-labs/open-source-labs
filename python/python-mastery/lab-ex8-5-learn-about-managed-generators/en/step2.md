# Creating a Task Scheduler with Generators

In programming, a task scheduler is a crucial tool that helps manage and execute multiple tasks efficiently. In this section, we'll use generators to build a simple task scheduler that can run multiple generator functions concurrently. This will show you how generators can be managed to perform cooperative multitasking, which means tasks take turns to run and share the execution time.

First, you need to create a new file. Navigate to the `/home/labex/project` directory and create a file named `multitask.py`. This file will contain the code for our task scheduler.

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

Now, let's break down how this task scheduler works:

1. We use a `deque` (double-ended queue) to store our generator tasks. A `deque` is a data structure that allows you to add and remove elements from both ends efficiently. It's a great choice for our task queue because we need to add tasks to the end and remove them from the front.
2. The `run()` function is the heart of our task scheduler. It takes tasks from the queue one by one:
   - It resumes each task using `send(None)`. This is similar to using `next()` on a generator. It tells the generator to continue executing from where it left off.
   - After the task yields, it's added back to the end of the queue. This way, the task will get another chance to run later.
   - When a task completes (raises `StopIteration`), it's removed from the queue. This indicates that the task has finished its execution.
3. Each `yield` statement in our generator tasks acts as a pause point. When a generator reaches a `yield` statement, it pauses its execution and gives control back to the scheduler. This allows other tasks to run.

This approach implements cooperative multitasking. Each task voluntarily yields control back to the scheduler, allowing other tasks to run. This way, multiple tasks can share the execution time and run concurrently.
