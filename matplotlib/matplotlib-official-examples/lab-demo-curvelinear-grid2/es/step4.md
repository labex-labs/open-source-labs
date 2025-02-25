# Definir ejes y mostrar imagen

El cuarto paso es definir los ejes utilizando la instancia `grid_helper` creada en el Paso 3. También mostraremos una imagen utilizando la función `imshow`.

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
