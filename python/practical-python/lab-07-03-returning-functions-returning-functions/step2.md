# Local Variables

Observe how the inner function refers to variables defined by the outer
function.

```python
def add(x, y):
    def do_add():
        # `x` and `y` are defined above `add(x, y)`
        print('Adding', x, y)
        return x + y
    return do_add
```

Further observe that those variables are somehow kept alive after
`add()` has finished.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # Where are these values coming from?
7
```
