# Generate a dataset

We generate a dataset of shape (300, 300) with 5 biclusters and noise of 5 using `make_biclusters` function.

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
