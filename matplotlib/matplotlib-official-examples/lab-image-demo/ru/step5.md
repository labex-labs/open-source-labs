# Управление началом изображения

```python
# Specify whether images should be plotted with the array origin x[0, 0] in the upper left or lower right
x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
axs[0].set_title('синий цвет должен быть сверху')
axs[0].imshow(x, origin='upper', interpolation=interp)

axs[1].set_title('синий цвет должен быть снизу')
axs[1].imshow(x, origin='lower', interpolation=interp)
plt.show()
```
