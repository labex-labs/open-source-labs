# 生成随机数据

接下来，我们将使用 NumPy 生成两个随机数据数组。我们将使用这些数组来演示互相关和自相关。

```python
np.random.seed(19680801)
x, y = np.random.randn(2, 100)
```
