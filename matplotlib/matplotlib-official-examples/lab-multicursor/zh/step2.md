# 创建数据

接下来，我们将为绘图创建一些数据。在这个例子中，我们将创建三个频率不同的正弦波。

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)
```
