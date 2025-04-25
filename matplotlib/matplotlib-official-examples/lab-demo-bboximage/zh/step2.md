# 创建带文本的 BboxImage

我们首先创建一个带文本的 BboxImage。我们使用`text()`方法创建一个`text`对象，并将其添加到`ax1`对象中。然后，我们使用`add_artist()`方法创建一个`BboxImage`对象。我们将`text`对象的`get_window_extent`方法传递给`BboxImage`构造函数，以获取文本的边界框。我们还将形状为 (1, 256) 的一维数组传递给`BboxImage`构造函数的`data`参数，以创建一个图像。

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```
