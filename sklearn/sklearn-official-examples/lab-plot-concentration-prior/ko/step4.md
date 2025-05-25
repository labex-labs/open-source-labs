# 추정기 정의

이 단계에서는 두 개의 추정기를 정의합니다. 첫 번째 추정기는 Dirichlet 분포 사전을 사용하여 0 이 아닌 가중치를 갖는 구성 요소의 수를 설정합니다. 두 번째 추정기는 Dirichlet 과정 사전을 사용하여 구성 요소의 수를 선택합니다.

```python
estimators = [
    (
        "Dirichlet 분포 사전을 사용한 유한 혼합\n및 " r"$\gamma_0=$",
        BayesianGaussianMixture(
            weight_concentration_prior_type="dirichlet_distribution",
            n_components=2 * n_components,
            reg_covar=0,
            init_params="random",
            max_iter=1500,
            mean_precision_prior=0.8,
            random_state=random_state,
        ),
        [0.001, 1, 1000],
    ),
    (
        "Dirichlet 과정 사전을 사용한 무한 혼합\n및" r"$\gamma_0=$",
        BayesianGaussianMixture(
            weight_concentration_prior_type="dirichlet_process",
            n_components=2 * n_components,
            reg_covar=0,
            init_params="random",
            max_iter=1500,
            mean_precision_prior=0.8,
            random_state=random_state,
        ),
        [1, 1000, 100000],
    ),
]
```
