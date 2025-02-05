# 使用随机梯度下降（SGD）训练分类器

现在我们将使用SGDClassifier类训练一个分类器。我们将使用对数损失（log_loss）损失函数和L2正则化。

```python
# 使用随机梯度下降训练分类器
clf = SGDClassifier(loss="log_loss", penalty="l2", max_iter=100, random_state=42)
clf.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = clf.predict(X_test)

# 评估分类器的准确率
accuracy = accuracy_score(y_test, y_pred)

# 打印准确率
print("分类器准确率:", accuracy)
```
