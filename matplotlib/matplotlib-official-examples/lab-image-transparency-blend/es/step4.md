# Utilizar la transparencia para resaltar valores

Finalmente, recrearemos la misma gráfica, pero esta vez usaremos la transparencia para resaltar los valores extremos en los datos. Esto se suele utilizar para resaltar puntos de datos con valores p más pequeños. También agregaremos líneas de contorno para resaltar los valores de la imagen.

```python
# Crear un canal alfa basado en los valores de peso
alphas = Normalize(0,.3, clip=True)(np.abs(weights))
alphas = np.clip(alphas,.4, 1)  # el valor de alfa se recorta en la parte inferior en.4

# Crear la figura y la imagen
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# Agregar líneas de contorno para resaltar aún más diferentes niveles.
ax.contour(weights[::-1], levels=[-.1,.1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001,.0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```
