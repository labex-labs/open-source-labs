# 计算最近邻图

在这一步中，我们将使用KNeighborsTransformer计算最近邻图。

```python
# 该变换器使用网格搜索中所需的最大邻居数来计算最近邻图。分类器模型会根据其自身的n_neighbors参数要求对最近邻图进行筛选。
graph_model = KNeighborsTransformer(n_neighbors=max(n_neighbors_list), mode="distance")
```
