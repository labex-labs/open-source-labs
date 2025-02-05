# 使用“最近邻”插值对图像进行上采样

现在，我们将使用“最近邻”插值将图像从500个数据像素上采样到530个渲染像素。这将演示如果上采样因子不是整数，即使图像被上采样，莫尔条纹仍可能出现。

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
plt.show()
```
