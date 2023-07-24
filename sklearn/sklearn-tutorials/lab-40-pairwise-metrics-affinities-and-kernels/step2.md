# Kernels

Kernels are measures of similarity between two objects. They can be used in various machine learning algorithms to capture non-linear relationships between features.

Scikit-learn provides different kernel functions, such as linear kernel, polynomial kernel, sigmoid kernel, RBF kernel, Laplacian kernel, and chi-squared kernel.

Let's calculate the pairwise kernels between two sets of samples using the `pairwise_kernels` function:

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise kernels between X and Y using linear kernel
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

Output:

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```
