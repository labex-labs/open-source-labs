# 创建数据

接下来，我们需要创建用于生成等高线图的数据。我们将使用 `mpl_toolkits.mplot3d` 模块中的 `get_test_data()` 函数来生成示例数据。

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
