# 为图表创建数据

我们需要创建用于可视化的图表数据。在这个例子中，我们将使用 NumPy 创建三个不同的数据集。

```python
t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = np.sin(4 * np.pi * t)
```
