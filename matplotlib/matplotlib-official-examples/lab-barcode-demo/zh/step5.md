# 渲染条形码

最后，我们可以使用 `Axes.imshow` 来渲染条形码。我们将使用 `code.reshape(1, -1)` 把数据转换为一个只有一行的二维数组，使用 `imshow(..., aspect='auto')` 来处理非方形像素，以及使用 `imshow(..., interpolation='nearest')` 来防止边缘模糊。

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```
