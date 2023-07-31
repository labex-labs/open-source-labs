# Define Custom Ticker Function

Next, we need to define the custom ticker function. The custom ticker function takes two arguments - the value and tick position - and returns the formatted tick label. In this case, we will format the tick label as dollars in millions.

```python
def millions(x, pos):
    """The two arguments are the value and tick position."""
    return f'${x*1e-6:1.1f}M'
```
