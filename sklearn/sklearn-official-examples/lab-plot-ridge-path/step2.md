# Generate Data

In this step, we will generate a 10x10 Hilbert matrix and set the target variable y to be a vector of ones.

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
