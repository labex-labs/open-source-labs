# Testing Our Task Scheduler

Now, we're going to add a test to our `multitask.py` file. The purpose of this test is to run multiple tasks at the same time, which is known as concurrent execution. Concurrent execution allows different tasks to make progress seemingly at the same time, even though in a single-threaded environment, the tasks are actually taking turns to run.

To perform this test, add the following code at the end of the `multitask.py` file:

```python
# Test our scheduler
if __name__ == '__main__':
    # Add tasks to the queue
    tasks.append(countdown(10))  # Count down from 10
    tasks.append(countdown(5))   # Count down from 5
    tasks.append(countup(20))    # Count up to 20

    # Run all tasks
    run()
```

In this code, we first check if the script is being run directly using `if __name__ == '__main__':`. Then, we add three different tasks to the `tasks` queue. The `countdown` tasks will count down from the given numbers, and the `countup` task will count up to the specified number. Finally, we call the `run()` function to start executing these tasks.

After adding the code, run it with the following command in the terminal:

```bash
python3 /home/labex/project/multitask.py
```

When you run the code, you should see output similar to this (the exact order of the lines may vary):

```
T-minus 10
T-minus 5
Up we go 0
T-minus 9
T-minus 4
Up we go 1
T-minus 8
T-minus 3
Up we go 2
...
```

Notice how the output from the different tasks is mixed together. This is a clear indication that our scheduler is running all three tasks concurrently. Each time a task reaches a `yield` statement, the scheduler pauses that task and switches to another one, allowing all tasks to make progress over time.

## How It Works

Let's take a closer look at what happens when our scheduler runs:

1. First, we add three generator tasks to the queue: `countdown(10)`, `countdown(5)`, and `countup(20)`. These generator tasks are special functions that can pause and resume their execution at `yield` statements.
2. Then, the `run()` function starts its work:
   - It takes the first task, `countdown(10)`, from the queue.
   - It runs this task until it reaches a `yield` statement. When it hits the `yield`, it prints "T-minus 10".
   - After that, it adds the `countdown(10)` task back to the queue so that it can be run again later.
   - Next, it takes the `countdown(5)` task from the queue.
   - It runs the `countdown(5)` task until it hits a `yield` statement, printing "T-minus 5".
   - And this process continues...

This cycle keeps going until all tasks are finished. Each task gets a chance to run for a short while, which gives the illusion of concurrent execution without the need to use threads or callbacks. Threads are a more complex way of achieving concurrency, and callbacks are used in asynchronous programming. Our simple scheduler uses generators to achieve a similar effect in a more straightforward manner.
