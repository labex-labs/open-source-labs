# 数据预处理

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

我们将数据集拆分为训练集和测试集，并使用`StandardScaler()`函数对输入数据进行缩放，以此来预处理数据。
