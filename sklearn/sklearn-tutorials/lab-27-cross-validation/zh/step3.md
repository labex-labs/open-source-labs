# 将数据集拆分为训练集和测试集

为了评估我们模型的性能，我们需要将数据集拆分为训练集和测试集。我们将使用scikit-learn库中的`train_test_split`函数来完成此操作。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
