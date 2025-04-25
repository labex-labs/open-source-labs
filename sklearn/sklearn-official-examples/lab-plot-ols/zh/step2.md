# 分割数据集

接下来，我们将数据集分割为训练集和测试集。我们将使用 80% 的数据进行训练，20% 的数据进行测试。

```python
# 将数据分割为训练集/测试集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# 将目标分割为训练集/测试集
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```
