# 공분산 추정

두 번째 단계는 공분산을 추정하는 것입니다. 희소 정밀도 행렬을 학습하기 위해 GraphicalLassoCV 를 사용합니다. 또한 Ledoit-Wolf 추정기와 결과를 비교합니다.

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
