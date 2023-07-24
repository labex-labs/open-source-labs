# Simple Formatting

In this step, we will show how to use a simple formatter by passing a string or function to `~.Axis.set_major_formatter` or `~.Axis.set_minor_formatter`. We will create two plots, one using a string formatter and the other using a function formatter.

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Simple Formatting')

# A ``str``, using format string function syntax, can be used directly as a
# formatter.  The variable ``x`` is the tick value and the variable ``pos`` is
# tick position.  This creates a StrMethodFormatter automatically.
setup(axs0[0], title="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# A function can also be used directly as a formatter. The function must take
# two arguments: ``x`` for the tick value and ``pos`` for the tick position,
# and must return a ``str``. This creates a FuncFormatter automatically.
setup(axs0[1], title="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```
