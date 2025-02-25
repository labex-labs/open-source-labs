# Construir el diagrama de dispersión

Ahora, construiremos el diagrama de dispersión que actualizaremos durante la animación a medida que las gotas de lluvia evolucionen.

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```
