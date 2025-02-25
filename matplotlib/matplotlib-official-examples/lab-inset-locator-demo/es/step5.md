# Crear insets con posiciones arbitrarias

Podemos crear insets con posiciones arbitrarias usando el parámetro `bbox_to_anchor` para especificar un cuadro delimitador en coordenadas de datos y usando el parámetro `bbox_transform` para especificar la transformación para el cuadro delimitador.

```python
# Crea un inset en coordenadas de datos usando ax.transData como transformación
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```
