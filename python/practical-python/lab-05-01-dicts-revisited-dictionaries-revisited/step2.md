# Dicts and Modules

Within a module, a dictionary holds all of the global variables and
functions.

```python
# foo.py

x = 42
def bar():
    ...

def spam():
    ...
```

If you inspect `foo.__dict__` or `globals()`, you'll see the dictionary.

```python
{
    'x' : 42,
    'bar' : <function bar>,
    'spam' : <function spam>
}
```
