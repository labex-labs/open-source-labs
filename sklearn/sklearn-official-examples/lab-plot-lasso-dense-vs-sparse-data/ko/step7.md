# 희소 데이터에 대한 Lasso 학습

이제 밀집 데이터와 희소 데이터 각각에 대해 Lasso 회귀 모델을 두 개 학습합니다. alpha 매개변수를 0.1 로, 최대 반복 횟수를 10000 으로 설정합니다.

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```
