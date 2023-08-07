# Memory Revisited

In the CTA bus data, we determined that there were 181 unique bus routes.

```python
>>> routes = { row['route'] for row in rows }
>>> len(routes)
181
>>>
```

Question: How many unique route string objects are contained in the ride data? Instead of building a set of routes, build a set of object ids instead:

```python
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
542305
>>>
```

Think about this for a moment--there are only 181 distinct route names, but the resulting list of dictionaries contains 542305 different route strings. Maybe this is something that could be fixed with a bit of caching or object reuse. As it turns out, Python has a function that can be used to cache strings, `sys.intern()`. For example:

```python
>>> a = 'hello world'
>>> b = 'hello world'
>>> a is b
False
>>> import sys
>>> a = sys.intern(a)
>>> b = sys.intern(b)
>>> a is b
True
>>>
```

Restart Python and try this:

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, str, str, int])
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
181
>>>
````

Take a look at the memory use.

```python
>>> tracemalloc.get_traced_memory()
... look at result ...
>>>
```

The memory should drop quite a bit. Observation: There is a lot of repetition involving dates as well. What happens if you also cache the date strings?

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, str, int])
>>> tracemalloc.get_traced_memory()
... look at result ...
>>>
````
