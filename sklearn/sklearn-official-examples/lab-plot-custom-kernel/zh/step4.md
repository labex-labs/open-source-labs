# 创建支持向量机分类器

在这一步中，我们将创建一个支持向量机分类器实例并拟合我们的数据。我们将使用上一步中创建的自定义核函数。

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```
