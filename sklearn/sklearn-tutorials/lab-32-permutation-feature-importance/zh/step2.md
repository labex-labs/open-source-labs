# 训练模型

接下来，我们将在训练数据上训练一个回归模型。在这个例子中，我们将使用岭回归模型。

```python
from sklearn.linear_model import Ridge

# 训练岭回归模型
model = Ridge(alpha=1e-2).fit(X_train, y_train)
```
