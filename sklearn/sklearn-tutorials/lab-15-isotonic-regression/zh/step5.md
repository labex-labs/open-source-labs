# 可视化结果

最后，让我们可视化我们的保序回归模型的结果。我们可以将原始数据点绘制成散点，将预测值绘制成一条线。

```python
import matplotlib.pyplot as plt

# 绘制原始数据和预测值
plt.scatter(X, y, c='b', label='Original Data')
plt.plot(X_new, y_pred, c='r', label='Isotonic Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
