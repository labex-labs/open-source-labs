# 显示图像及其直方图

接下来，我们将使用Matplotlib的`imshow`函数显示图像，并使用`hist`显示其直方图。我们将创建一个包含两个子图的图形，一个用于显示图像，另一个用于显示直方图。

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```
