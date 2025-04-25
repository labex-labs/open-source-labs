# 不均衡問題

- SVM は、`class_weight` パラメータを調整することで不均衡問題を処理することができます：

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```
