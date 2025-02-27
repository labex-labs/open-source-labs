# Сжатие Ледоита-Вольфа

Метод сжатия Ледоита-Вольфа позволяет получить оптимальный коэффициент сжатия, минимизирующий среднеквадратичную ошибку между оцененной и истинной ковариационной матрицами. В пакете `sklearn.covariance` есть функция `ledoit_wolf`, которая может быть использована для вычисления оценщика Ледоита-Вольфа для заданного набора данных.

```python
from sklearn.covariance import ledoit_wolf

# Compute the Ledoit-Wolf estimator of the covariance matrix
ledoit_wolf_covariance_matrix = ledoit_wolf(data)[0]
```
