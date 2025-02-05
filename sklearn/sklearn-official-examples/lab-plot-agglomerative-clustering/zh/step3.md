# 创建一个图

创建一个捕捉局部连通性的图。邻居数量越多，聚类将越均匀，但会以计算时间为代价。邻居数量非常多会使聚类大小分布更均匀，但可能无法体现数据的局部流形结构。

```python
knn_graph = kneighbors_graph(X, 30, include_self=False)
```
