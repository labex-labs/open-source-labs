# 创建图形和图像

接下来，我们创建图形以及想要放置在其中的图像。在这个示例中，我们创建一个100x100的随机值数组，并将图像右半部分的值设置为1。然后，我们创建图像的两个单独实例，每个实例具有不同的位置和不透明度。

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```
