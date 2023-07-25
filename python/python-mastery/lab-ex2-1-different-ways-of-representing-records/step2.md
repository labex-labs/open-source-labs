# Basic memory use of text

Let's get a baseline of the memory required to work with this
datafile. First, restart Python and try a very simple experiment of
simply grabbing the file and storing its data in a single string:

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('ctabus.csv')
>>> tracemalloc.start()
>>> data = f.read()
>>> len(data)
12361039
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
12369664
>>> peak
24730766
>>>
```

Your results might vary somewhat, but you should see current
memory use in the range of 12MB with a peak of 24MB.

What happens if you read the entire file into a list of strings
instead? Restart Python and try this:

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('/home/labex/project/ctabus.csv')
>>> tracemalloc.start()
>>> lines = f.readlines()
>>> len(lines)
577564
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
45828030
>>> peak
45867371
>>>
```

You should see the memory use go up significantly into the range of 40-50MB.
Point to ponder: what might be the source of that extra overhead?
