# Эмпирическая ковариация

Эмпирическая ковариационная матрица - это широко используемый метод оценки ковариационной матрицы набора данных. Она основана на принципе максимального правдоподобия и предполагает, что наблюдения независимы и имеют одинаковое распределение (i.i.d.). Функция `empirical_covariance` из пакета `sklearn.covariance` может быть использована для вычисления эмпирической ковариационной матрицы заданного набора данных.

```python
from sklearn.covariance import empirical_covariance

# Compute the empirical covariance matrix
covariance_matrix = empirical_covariance(data)
```
