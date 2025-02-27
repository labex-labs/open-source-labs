# Verwende PCR mit 2 Komponenten

Wir verwenden PCR mit 2 Komponenten, um es mit PLS zu vergleichen.

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"PCR r-squared mit 2 Komponenten {pca_2.score(X_test, y_test):.3f}")
```
