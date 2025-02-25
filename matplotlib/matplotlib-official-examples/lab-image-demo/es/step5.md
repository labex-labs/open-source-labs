# Controlar el origen de la imagen

```python
# Especificar si las imágenes deben ser trazadas con el origen del arreglo x[0, 0] en la esquina superior izquierda o inferior derecha
x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
axs[0].set_title('blue should be up')
axs[0].imshow(x, origin='upper', interpolation=interp)

axs[1].set_title('blue should be down')
axs[1].imshow(x, origin='lower', interpolation=interp)
plt.show()
```
