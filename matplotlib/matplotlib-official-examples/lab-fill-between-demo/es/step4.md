# Marcando selectivamente regiones horizontales en todo el eje

El mismo mecanismo de selección se puede aplicar para rellenar toda la altura vertical del eje. Para ser independiente de los límites de y, agregamos una transformación que interpreta los valores de x en coordenadas de datos y los valores de y en coordenadas de eje. El siguiente ejemplo marca las regiones en las que los datos de y están por encima de un umbral dado.

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```
