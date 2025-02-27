# Оценка ковариации

Вторым шагом является оценка ковариации. Мы используем GraphicalLassoCV для обучения разреженной матрицы точности. Мы также сравниваем результаты с оценщиком Ledoit-Wolf.

```python
from sklearn.covariance import GraphicalLassoCV, ledoit_wolf

emp_cov = np.dot(X.T, X) / n_samples

model = GraphicalLassoCV()
model.fit(X)
cov_ = model.covariance_
prec_ = model.precision_

lw_cov_, _ = ledoit_wolf(X)
lw_prec_ = linalg.inv(lw_cov_)
```
