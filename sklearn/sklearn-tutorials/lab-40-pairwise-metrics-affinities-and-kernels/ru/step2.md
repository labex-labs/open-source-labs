# Ядерные функции

Ядерные функции - это меры сходства между двумя объектами. Они могут быть использованы в различных алгоритмах машинного обучения для выявления нелинейных связей между признаками.

Scikit-learn предоставляет различные ядровые функции, такие как линейная ядровая функция, полиномиальная ядровая функция, сигмоидальная ядровая функция, RBF-ядро (радиально-базисная функция), Лапласиан-ядро и хи-квадратное ядро.

Посчитаем попарные ядра между двумя наборами образцов с использованием функции `pairwise_kernels`:

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise kernels between X and Y using linear kernel
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

Результат:

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```
