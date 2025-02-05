# 检查特定数据范围

有时，可能需要检查图像中的特定数据范围。我们可以通过使用 `imshow` 函数中的 `clim` 参数来调整颜色映射表的限制来做到这一点。这使我们能够专注于图像的特定区域，同时牺牲其他区域的细节。

```python
min_value, max_value = 100, 200
plt.imshow(img, clim=(min_value, max_value))
```
