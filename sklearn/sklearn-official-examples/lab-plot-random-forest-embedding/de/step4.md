# Visualisierung des Ergebnisses nach der Dimensionalitätsreduzierung mit Truncated SVD

In diesem Schritt werden wir das Ergebnis nach der Dimensionalitätsreduzierung mit Truncated SVD visualisieren.

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```
