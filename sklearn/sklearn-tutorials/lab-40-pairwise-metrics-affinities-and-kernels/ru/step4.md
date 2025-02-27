# Полиномиальное ядро

Полиномиальное ядро вычисляет сходство между двумя векторами, учитывая взаимодействия между их измерениями.

Scikit-learn предоставляет функцию `polynomial_kernel` для вычисления полиномиального ядра между векторами.

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute polynomial kernel between X and Y
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

Результат:

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```
