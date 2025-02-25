# Personalizar el gráfico

Podemos personalizar el gráfico agregando etiquetas a los ejes y ajustando el ángulo de visualización.

```python
ax.set_xlabel('Etiqueta de X')
ax.set_ylabel('Etiqueta de Y')
ax.set_zlabel('Etiqueta de Z')
ax.view_init(elev=30, azim=120)
```
