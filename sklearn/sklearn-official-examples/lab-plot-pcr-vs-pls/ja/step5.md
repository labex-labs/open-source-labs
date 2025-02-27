# 2 主成分を使用した PCR

PLS と比較するために、2 主成分を使用した PCR を使います。

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"PCR r-squared with 2 components {pca_2.score(X_test, y_test):.3f}")
```
