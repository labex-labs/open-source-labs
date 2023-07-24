# Shuffle the Data

To ensure randomness in our analysis, let's shuffle the order of the samples in our dataset.

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
