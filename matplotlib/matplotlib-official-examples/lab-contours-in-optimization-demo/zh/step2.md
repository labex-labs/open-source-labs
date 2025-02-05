# 设置测量向量和矩阵

接下来，设置测量向量和矩阵。设计盘面载荷和传动比。

```python
nx = 101
ny = 105

# 设置测量向量
xvec = np.linspace(0.001, 4.0, nx)
yvec = np.linspace(0.001, 4.0, ny)

# 设置测量矩阵。设计盘面载荷和传动比。
x1, x2 = np.meshgrid(xvec, yvec)
```
