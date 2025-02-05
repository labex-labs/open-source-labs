# 生成数据

现在我们将生成用于三维等高线图的数据。我们将使用 `axes3d.get_test_data()` 方法来生成数据。此方法为三维绘图生成测试数据。

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
