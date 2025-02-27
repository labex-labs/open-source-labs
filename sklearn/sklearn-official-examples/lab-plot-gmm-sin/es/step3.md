# Ajustar un modelo mixto gaussiano con EM

Ajustaremos un modelo mixto gaussiano clásico con 10 componentes utilizando el algoritmo de Expectación-Maximización.

```python
# Ajustar una mezcla gaussiana con EM utilizando diez componentes
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
