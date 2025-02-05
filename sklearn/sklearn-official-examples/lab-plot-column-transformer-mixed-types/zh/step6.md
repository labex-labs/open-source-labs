# 划分数据

在这一步中，我们将使用 `train_test_split` 把数据划分为训练集和测试集。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```
