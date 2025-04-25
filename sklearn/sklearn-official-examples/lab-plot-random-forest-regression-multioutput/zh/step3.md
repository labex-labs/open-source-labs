# 将数据拆分为训练集和测试集

我们将使用 scikit-learn 的`train_test_split`函数把数据拆分为一个包含 400 个样本的训练集和一个包含 200 个样本的测试集。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```
