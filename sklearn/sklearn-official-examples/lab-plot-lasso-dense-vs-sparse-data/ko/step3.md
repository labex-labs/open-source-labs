# 밀집 데이터에 Lasso 학습

이제 밀집 데이터와 희소 데이터에 각각 하나씩, 두 개의 Lasso 회귀 모델을 학습시킵니다. alpha 매개변수를 1 로 설정하고 최대 반복 횟수를 1000 으로 설정합니다.

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
