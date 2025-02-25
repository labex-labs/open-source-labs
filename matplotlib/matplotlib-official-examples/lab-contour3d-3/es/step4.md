# Proyectar perfiles de contorno sobre las paredes del gráfico

En este paso, proyectaremos perfiles de contorno sobre las paredes del gráfico trazando los contornos para cada dimensión con desplazamientos adecuados.

```python
# Traza las proyecciones de los contornos para cada dimensión
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
