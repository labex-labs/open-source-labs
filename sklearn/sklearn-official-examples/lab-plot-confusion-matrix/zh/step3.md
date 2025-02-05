# 划分数据

我们会将数据集划分为训练集和测试集。训练集用于训练模型，测试集用于评估模型的性能。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
