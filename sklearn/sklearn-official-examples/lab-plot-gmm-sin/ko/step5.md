# 디리클레 과정 사전을 사용한 베이지안 가우시안 혼합 모델 적합

이제 디리클레 과정 사전을 사용한 베이지안 가우시안 혼합 모델을 적합합니다. 모델이 활성 구성 요소의 수를 적게 선호하도록 농도 사전의 값을 낮게 설정합니다.

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e-2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="random",
    max_iter=100,
    random_state=2,
).fit(X)
```
