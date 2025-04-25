# 控制图像原点

```python
# 指定图像应以数组原点 x[0, 0] 位于左上角还是右下角的方式绘制
x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
axs[0].set_title('蓝色应在上部')
axs[0].imshow(x, origin='upper', interpolation=interp)

axs[1].set_title('蓝色应在下部')
axs[1].imshow(x, origin='lower', interpolation=interp)
plt.show()
```
