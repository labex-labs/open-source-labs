# 密度推定と新奇性検出

- SVMは、`OneClassSVM` クラスを使って密度推定と新奇性検出にも使用できます：

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```
