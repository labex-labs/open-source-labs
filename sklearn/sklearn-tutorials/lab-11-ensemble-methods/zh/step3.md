# 划分数据

我们将使用 scikit-learn 中的`train_test_split`函数把数据划分为训练集和测试集。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
