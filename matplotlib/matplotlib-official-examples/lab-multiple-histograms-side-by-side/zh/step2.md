# 创建示例数据集

接下来，我们将创建用于直方图的示例数据集。我们将创建三个数据集，每个数据集包含387个数据点：

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```
