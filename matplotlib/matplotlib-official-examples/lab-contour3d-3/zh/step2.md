# 创建 3D 图形和数据

在这一步中，我们将创建一个 3D 图形并获取用于曲面图的测试数据。

```python
# 创建一个 3D 图形
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 获取用于曲面图的测试数据
X, Y, Z = axes3d.get_test_data(0.05)
```
