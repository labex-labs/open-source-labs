# AIC 및 BIC 재스케일링

[ZHT2007]의 정의와 일치하도록 AIC 및 BIC 를 재스케일링해야 합니다.

```python
def zou_et_al_criterion_rescaling(criterion, n_samples, noise_variance):
    """Zou 등의 정의에 따라 정보 기준을 재스케일링합니다."""
    return criterion - n_samples * np.log(2 * np.pi * noise_variance) - n_samples

aic_criterion = zou_et_al_criterion_rescaling(
    lasso_lars_ic[-1].criterion_,
    n_samples,
    lasso_lars_ic[-1].noise_variance_,
)

index_alpha_path_aic = np.flatnonzero(
    lasso_lars_ic[-1].alphas_ == lasso_lars_ic[-1].alpha_
)[0]
```
