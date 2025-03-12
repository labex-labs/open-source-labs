# Testing Our Task Scheduler

Now let's add a test to our `multitask.py` file to run multiple tasks concurrently. Add the following code at the end of the file:

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

Run the code with:

```bash
python3 /home/labex/project/multitask.py
```

You should see output like this (the exact order may vary):

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

Notice how the output from the different tasks is interleaved. This demonstrates that our scheduler is running all three tasks concurrently, switching between them each time they yield.

## How It Works

Let's trace through what happens when our scheduler runs:

1. We add three generator tasks to the queue: `countdown(10)`, `countdown(5)`, and `countup(20)`
2. The `run()` function:
   - Takes `countdown(10)` from the queue
   - Runs it until it hits `yield` (printing "T-minus 10")
   - Adds it back to the queue
   - Takes `countdown(5)` from the queue
   - Runs it until it hits `yield` (printing "T-minus 5")
   - And so on...

This continues until all tasks are complete. Each task gets a chance to run, simulating concurrent execution without using threads or callbacks.
