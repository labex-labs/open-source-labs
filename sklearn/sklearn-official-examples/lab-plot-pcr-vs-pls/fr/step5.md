# Utiliser la PCR avec 2 composantes

Nous utilisons la PCR avec 2 composantes pour la comparer à la PLS.

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"PCR r-carré avec 2 composantes {pca_2.score(X_test, y_test):.3f}")
```
