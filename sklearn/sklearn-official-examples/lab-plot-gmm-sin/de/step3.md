# Ein Gaussian Mixture Model mit EM anpassen

Wir werden ein klassisches Gaussian Mixture Model mit 10 Komponenten anpassen, das mit dem Expectation-Maximization-Algorithmus angepasst wird.

```python
# Ein Gaussian mixture mit EM anpassen, indem zehn Komponenten verwendet werden
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
