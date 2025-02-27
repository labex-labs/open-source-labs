# Kernel Polinomial

El kernel polinomial calcula la similitud entre dos vectores considerando las interacciones entre sus dimensiones.

Scikit-learn proporciona la función `polynomial_kernel` para calcular el kernel polinomial entre vectores.

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute polynomial kernel between X and Y
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

Salida:

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```
