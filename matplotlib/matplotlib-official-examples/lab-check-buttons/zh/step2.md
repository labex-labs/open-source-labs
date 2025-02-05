# 生成数据

接下来，我们将为图表生成数据。我们将使用 `numpy` 创建三个频率不同的正弦波。

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)
```
