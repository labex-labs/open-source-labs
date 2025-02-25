# Crear la figura y los ejes

Necesitamos crear la figura y los ejes para el código de barras. Estableceremos el tamaño de la figura como un múltiplo del número de puntos de datos y desactivaremos todos los ejes.

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # abarcar toda la figura
ax.set_axis_off()
```
