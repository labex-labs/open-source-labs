# 生成数据集

我们将使用scikit-learn中的`make_blobs`函数生成一个三分类数据集。我们将使用1000个样本，并将数据点集的中心设置为`[-5, 0], [0, 1.5], [5, -1]`。然后，我们将使用一个变换矩阵对数据集进行变换，以使数据集更难分类。

```python
centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blobs(n_samples=1000, centers=centers, random_state=40)
transformation = [[0.4, 0.2], [-0.4, 1.2]]
X = np.dot(X, transformation)
```
