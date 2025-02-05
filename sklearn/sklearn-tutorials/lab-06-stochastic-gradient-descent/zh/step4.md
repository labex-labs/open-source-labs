# 划分数据

我们将把数据集划分为训练集和测试集。训练集将用于训练随机梯度下降（SGD）分类器，而测试集将用于评估其性能。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
