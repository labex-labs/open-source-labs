# Polynomial Kernel

The polynomial kernel calculates the similarity between two vectors by considering the interactions between their dimensions.

Scikit-learn provides the `polynomial_kernel` function to compute the polynomial kernel between vectors.

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute polynomial kernel between X and Y
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

Output:

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```
