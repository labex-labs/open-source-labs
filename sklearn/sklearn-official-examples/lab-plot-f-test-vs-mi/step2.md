# Create dataset

We will create a dataset with 3 features, where the first feature has a linear relationship with the target, the second feature has a non-linear relationship with the target, and the third feature is completely irrelevant. We will create 1000 samples for this dataset.

```python
np.random.seed(0)
X = np.random.rand(1000, 3)
y = X[:, 0] + np.sin(6 * np.pi * X[:, 1]) + 0.1 * np.random.randn(1000)
```


