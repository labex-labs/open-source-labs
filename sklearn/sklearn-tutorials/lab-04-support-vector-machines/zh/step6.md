# 密度估计与异常检测

- 支持向量机（SVM）还可通过 `OneClassSVM` 类用于密度估计和异常检测：

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```
