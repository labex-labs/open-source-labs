# Creando un diagrama de caja rectangular

Ahora crearemos un diagrama de caja rectangular utilizando la función `boxplot()` en Matplotlib. Estableceremos el parámetro `patch_artist` en `True` para rellenar la caja con color.

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # alineación vertical de la caja
                     patch_artist=True,  # rellenar con color
                     labels=labels)  # etiquetas de las marcas del eje x
ax1.set_title('Diagrama de caja rectangular')
```
