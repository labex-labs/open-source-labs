# 创建数据

在这一步中，我们创建将用于绘制误差线图的数据。

```python
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)
```
