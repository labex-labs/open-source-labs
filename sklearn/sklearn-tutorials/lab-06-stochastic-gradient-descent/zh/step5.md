# 训练分类器

现在我们可以使用 scikit-learn 的 SGDClassifier 类来创建并训练随机梯度下降（SGD）分类器。我们将使用“铰链”损失函数，它通常用于线性分类器。

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```
