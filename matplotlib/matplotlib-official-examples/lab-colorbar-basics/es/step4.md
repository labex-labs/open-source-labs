# Crear un gráfico y una barra de color para datos negativos

Creamos un gráfico de los datos negativos y agregamos una barra de color al gráfico usando la función `colorbar`. Esta vez, especificamos la ubicación de la barra de color, así como los parámetros de anclaje y encogimiento.

```python
# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
