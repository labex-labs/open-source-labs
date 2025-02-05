# 使用透明度突出显示值

最后，我们将重新创建相同的绘图，但这次我们将使用透明度来突出显示数据中的极值。这通常用于突出显示p值较小的数据点。我们还将添加等高线以突出显示图像值。

```python
# 根据权重值创建一个透明度通道
alphas = Normalize(0,.3, clip=True)(np.abs(weights))
alphas = np.clip(alphas,.4, 1)  # 透明度值在底部裁剪为.4

# 创建图形和图像
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# 添加等高线以进一步突出显示不同级别。
ax.contour(weights[::-1], levels=[-.1,.1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001,.0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```
