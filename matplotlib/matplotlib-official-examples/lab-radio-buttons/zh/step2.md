# 创建数据

接下来，我们将创建绘图中要使用的数据。我们将使用 `numpy` 库创建三个频率不同的正弦波。

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```
