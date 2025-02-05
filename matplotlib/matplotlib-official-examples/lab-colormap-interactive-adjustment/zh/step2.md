# 生成数据

接下来，你将生成一些示例数据。在本实验中，我们将生成一个二维正弦波。

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```
