# Closing a Generator

A common question concerning generators is their lifetime and garbage
collection. For example, the `follow()` generator runs forever in
an infinite `while` loop. What happens if the iteration loop that's
driving it stops? Also, is there anyway to prematurely terminate the
generator?

Modify the `follow()` function so that all of the code is enclosed in
a `try-except` block like this:

```python
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

Now, try a few experiments:

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f
Following Done
>>> # Experiment: Closing a generator
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            f.close()

"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
...
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
        print(line, end='')    # No output: generator is done

>>>
```

In these experiments you can see that a `GeneratorExit` exception is
raised when a generator is garbage-collected or explicitly closed via
its `close()` method.

One additional area of exploration is whether or not you can resume
iteration on a generator if you break out of a for-loop. For example,
try this:

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
...
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> # Resume iteration
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"AA",39.58,"6/11/2007","09:39.28",-0.08,39.67,39.58,39.31,243159
"HPQ",45.94,"6/11/2007","09:39.29",0.24,45.80,45.94,45.59,408919
...
"IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
>>> del f
Following Done
>>>
```

In general, you can break out of running iteration and resume it later
if you need to. You just need to make sure the generator object isn't
forcefully closed or garbage collected somehow.
