# Realizar Aglomeração de Recursos

Neste passo, realizaremos a aglomeração de recursos utilizando a classe `FeatureAgglomeration` do scikit-learn. Definiremos o número de clusters como 32.

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
