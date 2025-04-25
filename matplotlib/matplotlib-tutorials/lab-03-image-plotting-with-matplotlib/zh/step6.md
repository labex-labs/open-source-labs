# 数组插值方案

在调整图像大小时，需要对像素值进行插值以填充缺失的空间。可以使用不同的插值方案根据其周围像素来确定像素的值。Matplotlib 提供了不同的插值选项，例如“nearest”（最近邻）、“bilinear”（双线性）和“bicubic”（双三次）。

```python
plt.imshow(img, interpolation="bilinear")
```
