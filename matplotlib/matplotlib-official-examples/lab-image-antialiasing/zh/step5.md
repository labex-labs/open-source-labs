# 使用“抗锯齿”插值对图像进行上采样

最后，我们将使用“抗锯齿”插值把图像从500个数据像素上采样到530个渲染像素。这将展示使用更好的抗锯齿算法如何减少莫尔条纹。

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.show()
```
