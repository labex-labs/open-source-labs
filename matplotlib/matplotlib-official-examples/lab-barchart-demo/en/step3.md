# Define Helper Functions

We define two helper functions. The first function, `to_ordinal`, converts an integer to an ordinal string (e.g. 2 -> '2nd'). The second function, `format_score`, creates score labels for the right y-axis as the test name followed by the measurement unit (if any), split over two lines.

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
