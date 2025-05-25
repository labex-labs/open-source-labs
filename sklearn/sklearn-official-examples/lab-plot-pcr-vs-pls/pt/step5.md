# Usar PCR com 2 Componentes

Usamos PCR com 2 componentes para compará-lo com PLS.

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"PCR r-squared com 2 componentes {pca_2.score(X_test, y_test):.3f}")
```
