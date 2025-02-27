# Usar PCR con 2 componentes

Usamos PCR con 2 componentes para compararlo con PLS.

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"Coeficiente de determinación de PCR con 2 componentes {pca_2.score(X_test, y_test):.3f}")
```
