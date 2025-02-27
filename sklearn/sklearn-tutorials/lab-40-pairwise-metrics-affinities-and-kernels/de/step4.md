# Polynomkernel

Der Polynomkernel berechnet die Ähnlichkeit zwischen zwei Vektoren, indem er die Wechselwirkungen zwischen ihren Dimensionen berücksichtigt.

Scikit-learn bietet die Funktion `polynomial_kernel` an, um den Polynomkernel zwischen Vektoren zu berechnen.

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute polynomial kernel between X and Y
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

Ausgabe:

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```
