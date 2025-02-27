# Оценка устойчивой матрицы ковариации

В этом шаге мы оцениваем устойчивую матрицу ковариации набора данных с использованием оценщика минимального детерминанта ковариации (MCD).

```python
# Estimate a robust covariance matrix of the dataset
mcd = MinCovDet().fit(X)
robust_cov = mcd.covariance_
```
