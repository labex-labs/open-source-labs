# 创建数据

接下来，我们将为绘图创建数据。我们将使用 `numpy` 库创建一个正弦波。

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
```
