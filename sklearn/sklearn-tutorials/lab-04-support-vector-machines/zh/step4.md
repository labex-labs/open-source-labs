# 不平衡问题

- 支持向量机（SVM）可以通过调整 `class_weight` 参数来处理不平衡问题：

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```
