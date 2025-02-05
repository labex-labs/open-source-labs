# 训练模型

在这一步中，我们将使用生成的数据训练带有径向基函数（RBF）内核的支持向量机分类器。

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```
