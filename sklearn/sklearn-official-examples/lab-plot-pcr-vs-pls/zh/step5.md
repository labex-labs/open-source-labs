# 使用具有两个主成分的主成分回归（PCR）

我们使用具有两个主成分的主成分回归（PCR）来与偏最小二乘回归（PLS）进行比较。

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"PCR r-squared with 2 components {pca_2.score(X_test, y_test):.3f}")
```
