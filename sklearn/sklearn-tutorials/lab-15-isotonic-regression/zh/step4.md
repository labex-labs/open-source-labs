# 使用模型进行预测

在拟合模型之后，我们可以使用它对新数据进行预测。让我们创建一个新的数组 `X_new` 并预测相应的目标值。

```python
# 创建用于预测的新数据
X_new = np.linspace(0, 1, 100)
y_pred = ir.predict(X_new)
```
