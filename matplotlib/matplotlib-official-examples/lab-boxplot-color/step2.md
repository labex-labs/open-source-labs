# Creating Random Test Data

Next, we will create random test data using the `numpy` library. We will generate 3 sets of data, each with a different standard deviation.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```
