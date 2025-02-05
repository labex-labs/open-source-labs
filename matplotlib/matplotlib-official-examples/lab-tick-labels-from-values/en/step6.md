# Set the tick formatter and locator

We set the x-axis tick formatter to the formatting function created in Step 5 using the `set_major_formatter()` method. We also set the x-axis tick locator to `MaxNLocator(integer=True)` to ensure that the tick values take integer values.

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```
