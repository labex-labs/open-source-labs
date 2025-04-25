# 分割数据集

我们将使用`sklearn.model_selection`中的`train_test_split()`方法将数据集分割为 50% 的训练子集和 50% 的测试子集。

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```
