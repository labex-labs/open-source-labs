# Using a Callable for Formatter

Instead of passing a function into `.Axis.set_major_formatter`, we can use any other callable, such as an instance of a class that implements `__call__`. In this step, we will create a class `MyFormatter` that formats the tick marks as times.

```python
# Use a callable for formatter
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Return the label for time x at position pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```
