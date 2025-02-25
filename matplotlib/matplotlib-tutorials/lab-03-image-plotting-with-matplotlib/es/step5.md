# Examinando rangos de datos específicos

A veces, puede ser necesario examinar rangos de datos específicos en una imagen. Esto se puede hacer ajustando los límites del mapa de colores utilizando el parámetro `clim` en la función `imshow`. Esto nos permite centrar la atención en regiones específicas de la imagen mientras sacrificamos detalles en otras regiones.

```python
min_value, max_value = 100, 200
plt.imshow(img, clim=(min_value, max_value))
```
