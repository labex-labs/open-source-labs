# 为椭圆创建数据

我们以 x 坐标、y 坐标、宽度、高度和角度的数组形式为椭圆创建数据。

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
