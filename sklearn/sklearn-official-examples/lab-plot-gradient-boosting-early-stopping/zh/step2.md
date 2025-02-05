# 准备数据

接下来，我们将通过将数据拆分为训练集和测试集来准备数据。

```python
for X, y in data_list:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
```
