# Crear el diagrama de contorno

Ahora crearemos el diagrama de contorno utilizando la función `contour()`. Pasaremos los datos `X`, `Y` y `Z`, y estableceremos `extend3d=True` para extender las curvas verticalmente en "cintas". También estableceremos el mapa de colores en `cm.coolwarm` para un bonito esquema de colores.

```python
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
```
