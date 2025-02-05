# 定义数据

在这一步中，我们将定义用于创建三维茎叶图的数据。我们将为角度创建一个线性间距数组，并使用正弦和余弦函数来计算 x 和 y 坐标。我们还将把 z 坐标定义为角度。

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```
