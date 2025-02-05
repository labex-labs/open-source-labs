# 图像旁边的常规绘图

当在常规绘图旁边创建具有固定数据纵横比且默认 `adjustable="box"` 的图像绘图时，坐标轴的高度会不一致。`set_box_aspect()` 提供了一个简单的解决方案，允许常规绘图的坐标轴使用图像的尺寸作为框体纵横比。此示例还展示了 _约束布局（constrained layout）_ 与固定框体纵横比能够很好地配合使用。

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```
