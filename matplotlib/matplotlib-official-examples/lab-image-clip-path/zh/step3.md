# 显示图像

现在我们可以使用 Matplotlib 的 `imshow` 方法来显示图像。我们还将关闭坐标轴，这样就只会看到图像。

```python
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')
```
