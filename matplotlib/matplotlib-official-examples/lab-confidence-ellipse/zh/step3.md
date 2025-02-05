# 定义 `get_correlated_dataset` 函数

我们还需要一个函数来生成具有指定均值、维度和相关性的二维数据集。

```python
def get_correlated_dataset(n, dependency, mu, scale):
    """
    创建一个具有指定二维均值 (mu) 和维度 (scale) 的随机二维数据集。
    相关性可以通过参数 'dependency'（一个 2x2 矩阵）来控制。
    """
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # 返回新的、相关数据集的 x 和 y
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
```
