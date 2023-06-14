# Use PCR with 2 Components

We use PCR with 2 components to compare it with PLS.

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"PCR r-squared with 2 components {pca_2.score(X_test, y_test):.3f}")
```
