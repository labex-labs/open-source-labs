# EM 알고리즘을 사용한 가우시안 혼합 모델 적합

10 개의 구성 요소를 가진 고전적인 가우시안 혼합 모델을 EM 알고리즘으로 적합합니다.

```python
# EM 알고리즘을 사용하여 10 개의 구성 요소로 가우시안 혼합 모델 적합
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
