# Crear el gráfico tridimensional

Usamos `subplot_mosaic` para crear el gráfico tridimensional basado en el diseño definido en el paso 4.

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
