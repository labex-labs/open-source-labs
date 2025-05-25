# Ajustar um Modelo de Mistura Gaussiana com EM

Ajustaremos um modelo clássico de Mistura Gaussiana com 10 componentes, ajustado com o algoritmo Expectation-Maximization.

```python
# Ajustar uma mistura gaussiana com EM usando dez componentes
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
