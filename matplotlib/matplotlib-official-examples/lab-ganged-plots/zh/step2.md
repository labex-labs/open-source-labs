# 生成数据

我们生成一些要绘制的示例数据。在这里，我们使用 `numpy` 库生成三个数据数组。

```python
t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2
```
