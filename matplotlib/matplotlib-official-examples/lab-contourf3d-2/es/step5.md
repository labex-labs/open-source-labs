# Proyectar perfiles de contorno

Ahora proyectaremos los perfiles de contorno sobre las paredes del gráfico. Esto se hace utilizando el método `contourf`. Estableceremos el parámetro `zdir` en 'z', 'x' e 'y' para proyectar los perfiles de contorno sobre las paredes z, x e y respectivamente. También estableceremos el parámetro `offset` para ajustar los límites de los ejes adecuados.

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
