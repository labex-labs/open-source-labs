# 加载并预处理数据

接下来，我们将加载鸢尾花数据集，并使用 StandardScaler 对特征进行缩放来预处理数据。

```python
# 加载鸢尾花数据集
iris = load_iris()
X, y = iris.data, iris.target

# 缩放特征
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 将数据拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```
