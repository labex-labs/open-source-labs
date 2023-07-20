# Create the Dataset

In this step, we will create a dataset with a continuous input feature and a continuous output feature. We will use the `numpy.random.RandomState()` method to generate random numbers for the input feature, and the `numpy.sin()` method to generate the output feature.

```python
rnd = np.random.RandomState(42)
X = rnd.uniform(-3, 3, size=100)
y = np.sin(X) + rnd.normal(size=len(X)) / 3
X = X.reshape(-1, 1)
```
