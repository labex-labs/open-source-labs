# Benutzerdefinierten Kernel erstellen

In diesem Schritt werden wir einen benutzerdefinierten Kernel erstellen. Der benutzerdefinierte Kernel wird ein Skalarprodukt zweier Matrizen sein. Wir werden eine Matrix M mit den Werten [[2, 0], [0, 1.0]] erstellen. Anschließend werden wir die Matrizen X und Y mit M multiplizieren und ihr Skalarprodukt bilden.

```python
def my_kernel(X, Y):
    """
    Wir erstellen einen benutzerdefinierten Kernel:

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    return np.dot(np.dot(X, M), Y.T)
```
