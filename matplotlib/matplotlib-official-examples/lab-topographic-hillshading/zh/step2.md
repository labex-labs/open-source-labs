# 加载数据

接下来，我们使用 Matplotlib 的`get_sample_data`函数加载示例海拔数据。然后，我们提取海拔数据和网格的像元大小。

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
