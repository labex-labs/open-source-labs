# 设置颜色

现在我们将为体素图中的每个对象设置颜色。我们通过创建一个与在步骤 3 中创建的布尔数组形状相同的空数组来实现，然后根据每个对象的位置设置其颜色。

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```
