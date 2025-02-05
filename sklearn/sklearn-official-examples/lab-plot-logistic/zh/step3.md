# 拟合分类器

生成数据集后，我们将使用 scikit-learn 中的 `LogisticRegression` 来拟合分类器。

```python
# 拟合分类器
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```
