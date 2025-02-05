# 划分数据

我们将使用 `train_test_split` 函数把数据集划分为训练集和测试集。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
