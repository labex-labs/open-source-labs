# Сокращенная ковариация

Максимальный правдоподобие оцениватель, хотя и несмещенный, может не точно оценивать собственные значения ковариационной матрицы, что приводит к неточным результатам. Чтобы уменьшить этот недостаток, используется метод сжатия (shrinkage). Сжатие уменьшает соотношение между наименьшим и наибольшим собственными значениями эмпирической ковариационной матрицы, повышая точность оценки. В пакете `sklearn.covariance` есть класс `ShrunkCovariance`, который можно использовать для подгонки сжатого оценивателя под данные.

```python
from sklearn.covariance import ShrunkCovariance

# Create a ShrunkCovariance object and fit it to the data
shrunk_estimator = ShrunkCovariance().fit(data)

# Compute the shrunk covariance matrix
shrunk_covariance_matrix = shrunk_estimator.covariance_
```
