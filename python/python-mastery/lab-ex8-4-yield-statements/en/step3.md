# Practical Applications of Generator Management

In this step, we're going to explore how to apply the concepts we've learned about managing generators and handling exceptions in generators to real - world scenarios. Understanding these practical applications will help you write more robust and efficient Python code.

## Creating a Robust File Monitoring System

Let's build a more reliable version of our file monitoring system. This system will be able to handle different situations, such as timeouts and user requests to stop.

First, open the WebIDE editor and create a new file named `robust_follow.py`. Here's the code you need to write in this file:

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

In this code, we first define a custom `TimeoutError` class. The `timeout_handler` function is used to raise this error when a timeout occurs. The `follow` function is a generator that reads a file and yields new lines. If a timeout is specified, it sets up an alarm using the `signal` module. If there's no new data in the file, it waits for a short time before trying again. The `try - except - finally` block is used to handle different exceptions and ensure proper cleanup.

After writing the code, save the file.

## Experimenting with the Robust File Monitoring System

Now, let's test our improved file monitoring system. Open a terminal and run the Python interpreter with the following commands:

```bash
cd ~/project
python3
```

### Experiment 1: Basic Usage

In the Python interpreter, we'll test the basic functionality of our `follow` generator. Here's the code to run:

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

Here, we import the `follow` function from our `robust_follow.py` file. Then we create a generator object `f` that follows the `stocklog.csv` file. We use a `for` loop to iterate over the lines yielded by the generator and print the first three lines.

### Experiment 2: Using Timeout

Let's see how the timeout feature works. Run the following code in the Python interpreter:

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

In this experiment, we create a generator with a 3 - second timeout. We process each line slowly by sleeping for 1 second between each line. After about 3 seconds, the generator raises a timeout exception, and the cleanup code in the `finally` block is executed.

### Experiment 3: Explicit Closure

Let's test how the generator handles an explicit closure. Run the following code:

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

Here, we create a generator and start iterating over its lines. After processing two lines, we explicitly close the generator using the `close` method. The generator then handles the `GeneratorExit` exception and performs the necessary cleanup.

## Creating a Data Processing Pipeline with Error Handling

Next, we'll create a simple data processing pipeline using coroutines. This pipeline will be able to handle errors at different stages.

Open the WebIDE editor and create a new file named `pipeline.py`. Here's the code to write in this file:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

In this code, the `consumer` decorator is used to initialize coroutines. The `grep` coroutine filters lines that contain a specific pattern and sends them to another coroutine. The `printer` coroutine prints the received items. The `follow_and_process` function reads a file, filters its lines using the `grep` coroutine, and prints the matching lines using the `printer` coroutine. It also handles the `KeyboardInterrupt` exception and ensures proper cleanup.

After writing the code, save the file.

## Testing the Data Processing Pipeline

Let's test our data processing pipeline. In a terminal, run the following command:

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

You should see output similar to this:

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

This output shows that the pipeline is working correctly, filtering and printing lines that contain the "IBM" pattern.

To stop the process, press `Ctrl+C`. You should see the following message:

```
Processing stopped by user
```

## Key Takeaways

1. Proper exception handling in generators allows you to create robust systems that can handle errors gracefully. This means your programs won't crash unexpectedly when something goes wrong.
2. You can use techniques like timeouts to prevent generators from running indefinitely. This helps manage system resources and ensures your program doesn't get stuck in an infinite loop.
3. Generators and coroutines can form powerful data processing pipelines where errors can be propagated and handled at the appropriate level. This makes it easier to build complex data processing systems.
4. The `finally` block in generators ensures cleanup operations are performed, regardless of how the generator terminates. This helps maintain the integrity of your program and prevents resource leaks.
