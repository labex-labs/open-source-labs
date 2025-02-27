# Definition der Kernfunktion

Als nächstes definieren wir die Kernfunktion. In diesem Beispiel verwenden wir die Radial Basis Function (RBF)-Kernfunktion. Wir definieren zwei Versionen der RBF-Kernfunktion: eine isotrope Version und eine anisotrope Version.

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```
