# 生成随机数据

我们将使用 NumPy 生成两组随机数据。这些数据将被绘制以创建一个散点图。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 200)
```
