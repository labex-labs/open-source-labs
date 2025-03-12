# Practical Applications of Generator Management

In this step, we will explore practical applications of the concepts we have learned about managing generators and handling exceptions in generators.

## Creating a Robust File Monitoring System

Let's create a more robust version of our file monitoring system that can handle various scenarios.

Create a new file named `robust_follow.py` in the WebIDE editor:

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

Save the file after creating it.

## Experimenting with the Robust File Monitoring System

Let's test our improved file monitoring system. Open a terminal and run the Python interpreter:

```bash
cd ~/project
python3
```

### Experiment 1: Basic Usage

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

### Experiment 2: Using Timeout

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

After about 3 seconds, the generator raises a timeout exception and performs cleanup.

### Experiment 3: Explicit Closure

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

When we explicitly close the generator, it handles the `GeneratorExit` exception and performs the necessary cleanup.

## Creating a Data Processing Pipeline with Error Handling

Now, let's create a simple data processing pipeline using coroutines that can handle errors at various stages.

Create a new file named `pipeline.py` in the WebIDE editor:

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

Save the file after creating it.

## Testing the Data Processing Pipeline

Let's test our data processing pipeline. In a terminal, run:

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

You should see output like:

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

Press `Ctrl+C` to stop the process. You should see the message:

```
Processing stopped by user
```

## Key Takeaways

1. Proper exception handling in generators allows you to create robust systems that can handle errors gracefully.
2. You can use techniques like timeouts to prevent generators from running indefinitely.
3. Generators and coroutines can form powerful data processing pipelines where errors can be propagated and handled at the appropriate level.
4. The `finally` block in generators ensures cleanup operations are performed, regardless of how the generator terminates.
