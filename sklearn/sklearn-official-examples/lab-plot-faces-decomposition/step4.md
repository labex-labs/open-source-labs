# Independent components - FastICA

Independent Component Analysis (ICA) is a method for separating multivariate signals into additive subcomponents that are maximally independent. We apply FastICA, which is a fast and robust algorithm for ICA.

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


