# Crear un gráfico con datos positivos y negativos

Creamos un gráfico con datos tanto positivos como negativos, y agregamos una barra de color al gráfico usando la función `colorbar`. Esta vez, especificamos los valores mínimo y máximo para la barra de color usando los parámetros `vmin` y `vmax`.

```python
# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
