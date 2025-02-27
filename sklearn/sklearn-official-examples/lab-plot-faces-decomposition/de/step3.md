# Nichtnegative Komponenten - NMF

Als nächstes wenden wir die Nichtnegative Matrix Faktorisierung (NMF) an, die die Datenmatrix in zwei nichtnegative Matrizen zerlegt, wobei eine die Basisvektoren und die andere die Koeffizienten enthält. Dies führt zu einer teilenbasierten Darstellung der Daten.

```python
# Non-negative components - NMF
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # original non- negative dataset
plot_gallery("Non-negative components - NMF", nmf_estimator.components_[:n_components])
```
