# 融入透明度

使用 `imshow` 绘制数据时，包含透明度的最简单方法是将与数据形状匹配的数组传递给 `alpha` 参数。

```python
# 创建一个向右线性递增的透明度通道。
alphas = np.ones(weights.shape)
alphas[:, 30:] = np.linspace(1, 0, 70)

# 创建图形和图像
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)
ax.set_axis_off()
plt.show()
```
