# Creating Random Array

Next, we will create a random array with dimensions (20, 20) using the `numpy.random.randn` function. We will also set a few elements to zero to create a sparse matrix.

```python
np.random.seed(19680801)
x = np.random.randn(20, 20)
x[5, :] = 0.
x[:, 12] = 0.
```
