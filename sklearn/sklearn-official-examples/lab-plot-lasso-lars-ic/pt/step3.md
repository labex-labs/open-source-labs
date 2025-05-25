# Redimensionar AIC e BIC

Precisamos redimensionar o AIC e o BIC para estar alinhado com a definição em [ZHT2007]\_.

```python
def zou_et_al_criterion_rescaling(criterion, n_samples, noise_variance):
    """Redimensionar o critério de informação para seguir a definição de Zou et al."""
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
