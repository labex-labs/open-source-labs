# 加载数据

接下来，我们将加载本教程中要使用的示例数据。我们将使用 `jacksboro_fault_dem.npz` 文件，其中包含海拔数据。

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
