# Working with Futures for Concurrent Programming

In Python, when you have a need to run functions at the same time, or concurrently, the language offers useful tools like threads and processes. But here's a common problem you'll face: how can you get the value that a function returns when it's running in a different thread? This is where the concept of a `Future` becomes very important.

A `Future` is like a placeholder for a result that will be available later. It's a way to represent a value that a function will produce in the future, even before the function has finished running. Let's understand this concept better with a simple example.

### Step 1: Create a New File

First, you need to create a new Python file. We'll call it `futures_demo.py`. You can use the following command in your terminal to create this file:

```
touch ~/project/futures_demo.py
```

### Step 2: Add Basic Function Code

Now, open the `futures_demo.py` file and add the following Python code. This code defines a simple function and shows how a normal function call works.

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

In this code, the `worker` function takes two numbers, adds them together, but first it simulates a time - consuming task by pausing for 5 seconds. When you call this function in a normal way, the program waits for the function to finish and then gets the return value.

### Step 3: Run the Basic Code

Save the file and run it using the following command in your terminal:

```
python ~/project/futures_demo.py
```

You should see the output like this:

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

This shows that a normal function call waits for the function to finish and then returns the result.

### Step 4: Run the Function in a Separate Thread

Next, let's see what happens when we run the `worker` function in a separate thread. Add the following code to the `futures_demo.py` file:

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

Here, we're using the `threading.Thread` class to start the `worker` function in a new thread. The main thread doesn't wait for the `worker` function to finish and continues its execution. However, when the `worker` thread finishes, we have no easy way to get the return value.

### Step 5: Run the Threaded Code

Save the file again and run it using the same command:

```
python ~/project/futures_demo.py
```

You'll notice that the main thread continues, the worker thread runs, but we can't access the return value of the `worker` function.

### Step 6: Use a `Future` Manually

To solve the problem of getting the return value from a thread, we can use a `Future` object. Add the following code to the `futures_demo.py` file:

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

In this code, we create a `Future` object and pass it to a new function `do_work_with_future`. This function calls the `worker` function and then sets the result in the `Future` object. The main thread can then use the `result()` method of the `Future` object to get the result when it's available.

### Step 7: Run the Code with `Future`

Save the file and run it again:

```
python ~/project/futures_demo.py
```

Now you'll see that we can successfully get the return value from the function running in the thread.

### Step 8: Use `ThreadPoolExecutor`

The `ThreadPoolExecutor` class in Python makes working with concurrent tasks even easier. Add the following code to the `futures_demo.py` file:

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

The `ThreadPoolExecutor` takes care of creating and managing the `Future` objects for you. You just need to submit the function and its arguments, and it will return a `Future` object that you can use to get the result.

### Step 9: Run the Complete Code

Save the file one last time and run it:

```
python ~/project/futures_demo.py
```

### Explanation

1. **Normal Function Call**: When you call a function in the normal way, the program waits for the function to finish and directly gets the return value.
2. **Thread Problem**: Running a function in a separate thread has a drawback. There's no built - in way to get the return value of the function running in that thread.
3. **Manual Future**: By creating a `Future` object and passing it to the thread, we can set the result in the `Future` and then get the result from the main thread.
4. **ThreadPoolExecutor**: This class simplifies concurrent programming. It handles the creation and management of `Future` objects for you, making it easier to run functions concurrently and get their return values.

`Future` objects have several useful methods:

- `result()`: This method is used to get the result of the function. If the result is not ready yet, it will wait until it is.
- `done()`: You can use this method to check if the computation of the function is complete.
- `add_done_callback()`: This method allows you to register a function that will be called when the result is ready.

This pattern is very important in concurrent programming, especially when you need to get results from functions running in parallel.
