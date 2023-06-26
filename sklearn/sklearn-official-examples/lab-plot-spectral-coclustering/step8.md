# Rearrange the shuffled dataset

We rearrange the shuffled dataset to make the biclusters contiguous using `argsort()` function from numpy.

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
