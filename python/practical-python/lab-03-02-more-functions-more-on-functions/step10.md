# Modifying Globals

If you must modify a global variable you must declare it as such.

```python
name = 'Dave'

def spam():
    global name
    name = 'Guido' # Changes the global name above
```

The global declaration must appear before its use and the corresponding variable must exist in the same file as the function. Having seen this, know that it is considered poor form. In fact, try to avoid `global` entirely if you can. If you need a function to modify some kind of state outside of the function, it's better to use a class instead (more on this later).
