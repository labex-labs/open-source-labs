# 将图像转换为浮点数并重塑形状

我们将把图像转换为浮点数，并将其重塑为二维numpy数组，以便能够由K均值算法进行处理。

```python
# 转换为浮点数，而不是默认的8位整数编码。
china = np.array(china, dtype=np.float64) / 255

# 获取图像的尺寸
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# 将图像重塑为二维numpy数组
image_array = np.reshape(china, (w * h, d))
```
