# Crear un inset fuera del eje

Podemos crear un inset fuera del eje usando el parámetro `bbox_to_anchor` para especificar un cuadro delimitador en coordenadas de ejes que se extiende fuera del eje.

```python
# Crea un inset fuera del eje
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05,.6,.5,.4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```
