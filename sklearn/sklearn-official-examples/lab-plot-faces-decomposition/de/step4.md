# Unabhängige Komponenten - FastICA

Die Unabhängige Komponentenanalyse (ICA) ist eine Methode zur Trennung multivariate Signale in additive subkomponenten, die maximal unabhängig sind. Wir wenden FastICA an, was ein schnelles und robustes Verfahren für die ICA ist.

```python
# Independent components - FastICA
ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
plot_gallery(
    "Independent components - FastICA", ica_estimator.components_[:n_components]
)
```
