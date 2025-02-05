# 准备数据

我们将使用 NumPy 生成两个频率不同的正弦波。

```python
t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)
```
