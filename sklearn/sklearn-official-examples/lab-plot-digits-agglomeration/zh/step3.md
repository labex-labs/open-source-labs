# 定义连接矩阵

在这一步中，我们将使用 scikit-learn 中的`grid_to_graph`函数定义连接矩阵。此函数基于图像的像素网格创建一个连接图。

```python
connectivity = grid_to_graph(*images[0].shape)
```
