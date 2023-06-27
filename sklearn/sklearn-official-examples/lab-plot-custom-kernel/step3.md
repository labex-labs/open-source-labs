# Create Custom Kernel

In this step, we will create a custom kernel. The custom kernel will be a dot product of two matrices. We will create a matrix M with the values [[2, 0], [0, 1.0]]. We will then multiply the matrices X and Y with M and take their dot product.

```python
def my_kernel(X, Y):
    """
    We create a custom kernel:

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    return np.dot(np.dot(X, M), Y.T)
```
