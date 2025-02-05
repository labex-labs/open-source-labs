# 准备数据集

我们需要将图像展平，把每个形状为`(8, 8)`的二维灰度值数组转换为形状为`(64,)`的数组。这将为我们提供一个形状为`(n_samples, n_features)`的数据集，其中`n_samples`是图像的数量，`n_features`是每个图像中的像素总数。

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```
