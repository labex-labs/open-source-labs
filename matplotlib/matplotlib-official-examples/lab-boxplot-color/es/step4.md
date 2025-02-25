# Creando un diagrama de caja con muesca

Ahora crearemos un diagrama de caja con muesca con la función `boxplot()`. Estableceremos el parámetro `notch` en `True` para crear un diagrama de caja con muesca.

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # forma de la muesca
                     vert=True,  # alineación vertical de la caja
                     patch_artist=True,  # rellenar con color
                     labels=labels)  # etiquetas de las marcas del eje x
ax2.set_title('Diagrama de caja con muesca')
```
