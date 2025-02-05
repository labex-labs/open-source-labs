# 训练支持向量机

我们将使用`sklearn`中的`svm.SVC()`方法在训练样本上训练一个支持向量分类器。

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```
