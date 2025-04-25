# 创建数据

我们将创建一些数据，用于说明光栅化概念。

```python
d = np.arange(100).reshape(10, 10)  # 要进行颜色映射的值
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)  # 将 x 旋转 -theta
yy = x*np.sin(theta) + y*np.cos(theta)  # 将 y 旋转 -theta
```
