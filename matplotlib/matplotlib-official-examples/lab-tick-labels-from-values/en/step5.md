# Create a formatting function

We create a formatting function that determines the tick label from the value at the tick. If the tick value is an integer in the range of `xs`, the corresponding label from the `labels` list is returned. Otherwise, an empty string is returned.

```python
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''
```
