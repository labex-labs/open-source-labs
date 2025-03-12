# Working with Futures for Concurrent Programming

When you need to run functions concurrently (in parallel), Python provides mechanisms like threads and processes. However, there is a challenge: how do you get the return value from a function running in another thread?

This is where the concept of `Future` comes in. A `Future` represents a result that will be available at some point in the future.

Let's explore this concept with a simple example:

1. Create a new file called `futures_demo.py`:

```
touch ~/project/futures_demo.py
```

2. Add the following code:

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

3. Save and run this file to see how a normal function call works:

```
python ~/project/futures_demo.py
```

You should see the function executing and then returning the result:

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

4. Now let's see what happens when we run the function in a separate thread. Add the following code to the file:

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

5. Save and run the file again:

```
python ~/project/futures_demo.py
```

Notice that we can't access the return value from the thread.

6. Now, let's use a `Future` to solve this problem. Add the following code:

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

7. Save and run the file again. You'll see how we can now get the return value:

```
python ~/project/futures_demo.py
```

8. Finally, let's see how the `ThreadPoolExecutor` makes this easier. Add the following code:

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

9. Save and run the complete file:

```
python ~/project/futures_demo.py
```

**Explanation:**

1. **Normal Function Call**: The function runs and returns a value directly.
2. **Thread Problem**: When running a function in a separate thread, there's no built-in way to return the value.
3. **Manual Future**: We create a `Future` object and pass it to the thread, which sets the result.
4. **ThreadPoolExecutor**: This simplifies working with concurrent tasks by handling the `Future` creation and management for us.

`Future` objects have several useful methods:

- `result()`: Get the result (waits if not ready)
- `done()`: Check if the computation is complete
- `add_done_callback()`: Register a function to call when the result is ready

This pattern is crucial for concurrent programming where you need to get results from functions running in parallel.
