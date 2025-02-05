# 创建螺旋线

```python
nverts = 50
npts = 100

# 制作一些螺旋线
r = np.arange(nverts)
theta = np.linspace(0, 2*np.pi, nverts)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = np.column_stack([xx, yy])
```

下一步是使用Numpy创建螺旋线。我们将使用正弦和余弦函数来创建螺旋线。
