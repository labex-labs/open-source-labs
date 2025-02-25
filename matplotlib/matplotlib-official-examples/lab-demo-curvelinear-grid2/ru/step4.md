# Определить оси и отобразить изображение

Четвёртым шагом является определение осей с использованием экземпляра `grid_helper`, созданного на третьем шаге. Также мы будем отображать изображение с использованием функции `imshow`.

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
