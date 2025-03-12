# Understanding Generator Lifetime and Closure

In this step, you will learn about the lifetime of Python generators and how they can be properly closed.

## What is the `follow()` Generator?

Let's first examine the `follow.py` file in the project directory. This file contains a generator function called `follow()` that continuously reads lines from a file, yielding each line as it is read.

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

This generator reads a file and continuously yields new lines as they appear (similar to the Unix `tail -f` command). It runs in an infinite loop, which raises an important question: what happens when we stop using the generator or want to terminate it early?

## Modifying the Generator to Handle Closure

Modify the `follow()` function in `follow.py` to properly handle the case when the generator is closed. Add a `try-except` block that catches the `GeneratorExit` exception:

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

Save the file after making these changes.

## Experimenting with Generator Closure

Now let's perform some experiments to see how generators behave when they are garbage collected or explicitly closed.

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

When the generator object is deleted, it is automatically closed, triggering our `GeneratorExit` exception handler.

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

When we explicitly call `close()` on the generator, it also triggers the `GeneratorExit` exception handler, and the generator cannot be used anymore.

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

This experiment shows that you can break out of a generator's iteration and then resume it later, as long as the generator object is not garbage collected or explicitly closed.

## Key Takeaways

1. When a generator is closed (either through garbage collection or by calling `close()`), a `GeneratorExit` exception is raised inside the generator.
2. You can catch this exception to perform cleanup actions when the generator is closed.
3. Breaking out of a generator's iteration (with `break`) does not close the generator, allowing it to be resumed later.

Exit the Python interpreter by typing `exit()` or pressing `Ctrl+D`.
