# 评估模型

我们将通过计算多层感知器分类器（MLPClassifier）在训练集和测试集上的准确率来评估它。

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```
