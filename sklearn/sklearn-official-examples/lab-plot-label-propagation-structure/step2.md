# Generate Dataset

Next, we generate a dataset containing two concentric circles using `make_circles`. We assign labels to the dataset such that all samples are unknown except for two samples which belong to the outer and inner circles respectively.

```python
n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner
```
