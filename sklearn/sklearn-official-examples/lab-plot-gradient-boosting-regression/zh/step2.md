# 数据预处理

接下来，我们将分割数据集，使用 90% 的数据进行训练，其余数据用于测试。我们还将设置回归模型的参数。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=13)

params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
}
```
