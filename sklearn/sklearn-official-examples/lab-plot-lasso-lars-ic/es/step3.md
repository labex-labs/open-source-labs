# Reescalar AIC y BIC

Necesitamos reescalar el AIC y el BIC para que estén de acuerdo con la definición en [ZHT2007]\_.

```python
def zou_et_al_criterion_rescaling(criterion, n_samples, noise_variance):
    """Reescalar el criterio de información para seguir la definición de Zou et al."""
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
