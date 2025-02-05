# Create Row Labels

We will create row labels for the dataset to represent the number of years for which the loss has been recorded. We will use a list comprehension to create the row labels.

```python
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
```
