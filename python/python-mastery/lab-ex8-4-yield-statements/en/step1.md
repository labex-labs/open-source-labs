# Understanding Generator Lifetime and Closure

In this step, we're going to explore the lifetime of Python generators and learn how to close them properly. Generators in Python are a special type of iterator that allow you to generate a sequence of values on-the-fly, rather than computing them all at once and storing them in memory. This can be very useful when dealing with large datasets or infinite sequences.

## What is the `follow()` Generator?

Let's start by looking at the `follow.py` file in the project directory. This file contains a generator function named `follow()`. A generator function is defined like a normal function, but instead of using the `return` keyword, it uses `yield`. When a generator function is called, it returns a generator object, which you can iterate over to get the values it yields.

The `follow()` generator function continuously reads lines from a file and yields each line as it is read. This is similar to the Unix `tail -f` command, which continuously monitors a file for new lines.

Open the `follow.py` file in the WebIDE editor:

```python
import os
import time

def follow(filename):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)    # Sleep briefly to avoid busy wait
                continue
            yield line
```

In this code, the `with open(filename, 'r') as f` statement opens the file in read mode and ensures that it is properly closed when the block is exited. The `f.seek(0, os.SEEK_END)` line moves the file pointer to the end of the file, so that the generator starts reading from the end. The `while True` loop continuously reads lines from the file. If the line is empty, it means there are no new lines yet, so the program sleeps for 0.1 seconds to avoid a busy wait and then continues to the next iteration. If the line is not empty, it is yielded.

This generator runs in an infinite loop, which raises an important question: what happens when we stop using the generator or want to terminate it early?

## Modifying the Generator to Handle Closure

We need to modify the `follow()` function in `follow.py` to handle the case when the generator is closed properly. To do this, we'll add a `try-except` block that catches the `GeneratorExit` exception. The `GeneratorExit` exception is raised when a generator is closed, either by garbage collection or by calling the `close()` method.

```python
import os
import time

def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)    # Sleep briefly to avoid busy wait
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')
```

In this modified code, the `try` block contains the main logic of the generator. If a `GeneratorExit` exception is raised, the `except` block catches it and prints the message 'Following Done'. This is a simple way to perform cleanup actions when the generator is closed.

Save the file after making these changes.

## Experimenting with Generator Closure

Now, let's conduct some experiments to see how generators behave when they are garbage collected or explicitly closed.

Open a terminal and run the Python interpreter:

```bash
cd ~/project
python3
```

### Experiment 1: Garbage Collection of a Running Generator

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f  # Delete the generator object
Following Done  # This message appears because of our GeneratorExit handler
```

In this experiment, we first import the `follow` function from the `follow.py` file. Then we create a generator object `f` by calling `follow('stocklog.csv')`. We use the `next()` function to get the next line from the generator. Finally, we delete the generator object using the `del` statement. When the generator object is deleted, it is automatically closed, which triggers our `GeneratorExit` exception handler, and the message 'Following Done' is printed.

### Experiment 2: Explicitly Closing a Generator

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         f.close()  # Explicitly close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
...     print(line, end='')  # No output: generator is closed
...
```

In this experiment, we create a new generator object `f` and iterate over it using a `for` loop. Inside the loop, we print each line and check if the line contains the string 'IBM'. If it does, we call the `close()` method on the generator to explicitly close it. When the generator is closed, the `GeneratorExit` exception is raised, and our exception handler prints the message 'Following Done'. After the generator is closed, if we try to iterate over it again, there will be no output because the generator is no longer active.

### Experiment 3: Breaking Out of and Resuming a Generator

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break  # Break out of the loop, but don't close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
>>> # Resume iteration - the generator is still active
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break
...
"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> del f  # Clean up
Following Done
```

In this experiment, we create a generator object `f` and iterate over it using a `for` loop. Inside the loop, we print each line and check if the line contains the string 'IBM'. If it does, we use the `break` statement to break out of the loop. Breaking out of the loop does not close the generator, so the generator is still active. We can then resume the iteration by starting a new `for` loop over the same generator object. Finally, we delete the generator object to clean up, which triggers the `GeneratorExit` exception handler.

## Key Takeaways

1. When a generator is closed (either through garbage collection or by calling `close()`), a `GeneratorExit` exception is raised inside the generator.
2. You can catch this exception to perform cleanup actions when the generator is closed.
3. Breaking out of a generator's iteration (with `break`) does not close the generator, allowing it to be resumed later.

Exit the Python interpreter by typing `exit()` or pressing `Ctrl+D`.
