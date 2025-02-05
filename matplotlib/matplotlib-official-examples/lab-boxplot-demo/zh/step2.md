# 生成数据

接下来，我们将生成一些示例数据用于我们的箱线图。在本教程中，我们将使用以下数据：

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
