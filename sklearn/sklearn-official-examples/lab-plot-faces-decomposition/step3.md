# Non-negative components - NMF

Next, we apply Non-negative Matrix Factorization (NMF), which factorizes the data matrix into two non-negative matrices, one containing the basis vectors and the other containing the coefficients. This results in a parts-based representation of the data.

```python
# Non-negative components - NMF
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # original non- negative dataset
plot_gallery("Non-negative components - NMF", nmf_estimator.components_[:n_components])
```


