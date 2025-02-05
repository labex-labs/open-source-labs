# 训练模型

我们将创建两个支持向量机（SVM）模型。第一个模型不考虑样本权重，第二个模型将考虑我们刚刚创建的样本权重。

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
