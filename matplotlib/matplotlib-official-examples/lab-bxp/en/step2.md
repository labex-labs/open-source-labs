# Compute boxplot statistics

The `boxplot_stats()` function from `matplotlib.cbook` module computes the statistics required for the boxplot. We pass in the data and labels as parameters.

```python
# Compute boxplot stats
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
