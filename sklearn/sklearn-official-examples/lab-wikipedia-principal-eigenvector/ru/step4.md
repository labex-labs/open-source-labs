# Вычисление главного сингулярного вектора с использованием случайного SVD

Мы вычислим главные сингулярные векторы с использованием метода randomized_svd, реализованного в scikit-learn.

```python
from sklearn.decomposition import randomized_svd

print("Вычисление главных сингулярных векторов с использованием randomized_svd")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
