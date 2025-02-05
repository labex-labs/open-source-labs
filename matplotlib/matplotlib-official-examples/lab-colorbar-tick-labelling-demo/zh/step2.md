# 创建一个带有垂直颜色条的绘图

我们将从创建一个带有垂直颜色条的绘图开始。我们将使用 `numpy` 中的 `randn` 生成一些随机数据，并将值裁剪到 -1 到 1 的范围内。然后，我们将使用 `imshow` 和 `coolwarm` 颜色映射创建一个 `AxesImage` 对象。最后，我们将为绘图添加一个标题。

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
