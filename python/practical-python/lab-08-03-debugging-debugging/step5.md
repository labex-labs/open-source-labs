# The Python Debugger

You can manually launch the debugger inside a program.

```python
def some_function():
    ...
    breakpoint()      # Enter the debugger (Python 3.7+)
    ...
```

This starts the debugger at the `breakpoint()` call.

In earlier Python versions, you did this. You'll sometimes see this mentioned in other debugging guides.

```python
import pdb
...
pdb.set_trace()       # Instead of `breakpoint()`
...
```
