# Generate random data

We will generate a 3D array of random data using `numpy.random.random()`. We will use a seed value to ensure that the same set of data is generated each time the code is run.

```python
np.random.seed(19680801)
data = np.random.random((50, 50, 50))
```
