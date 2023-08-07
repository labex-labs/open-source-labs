# Example: Counting Things

Let's say you want to tabulate the total shares of each stock.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

There are two `IBM` entries and two `GOOG` entries in this list. The shares need to be combined together somehow.
