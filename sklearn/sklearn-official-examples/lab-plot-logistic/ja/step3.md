# 分類器を適合させる

データセットを生成した後、scikit - learnの`LogisticRegression`を使って分類器を適合させます。

```python
# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```
