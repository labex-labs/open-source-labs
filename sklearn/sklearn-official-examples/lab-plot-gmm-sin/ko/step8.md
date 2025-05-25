# 디리클레 과정 사전을 사용한 베이지안 가우시안 혼합 모델 적합

이제 디리클레 과정 사전을 사용한 베이지안 가우시안 혼합 모델을 적합합니다. 데이터의 미세한 구조를 더 자유롭게 모델링할 수 있도록 농도 사전의 값을 높게 설정합니다.

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="kmeans",
    max_iter=100,
    random_state=2,
).fit(X)
```
