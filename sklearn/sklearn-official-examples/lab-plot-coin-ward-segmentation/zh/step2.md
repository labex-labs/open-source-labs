# 定义数据结构

图像中的像素与其相邻像素相连。为了对图像执行层次聚类，我们需要定义数据的结构。我们可以使用 scikit-learn 的 `grid_to_graph` 函数来创建一个定义数据结构的连通性矩阵。

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```
