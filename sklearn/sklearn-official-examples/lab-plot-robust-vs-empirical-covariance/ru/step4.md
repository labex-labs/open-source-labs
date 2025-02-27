# Оценка эмпирической матрицы ковариации

В этом шаге мы оцениваем эмпирическую матрицу ковариации набора данных с использованием оценщика максимального правдоподобия (MLE).

```python
# Estimate an empirical covariance matrix of the dataset
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
