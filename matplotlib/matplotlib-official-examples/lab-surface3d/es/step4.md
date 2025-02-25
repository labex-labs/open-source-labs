# Trazar la superficie

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

Tracemos la superficie utilizando la función `plot_surface()`. Pasamos los valores de `X`, `Y` y `Z`, así como el parámetro `cmap` establecido en `cm.coolwarm` para colorear la superficie con la paleta de colores coolwarm. También establecemos `linewidth = 0` para eliminar el wireframe y `antialiased = False` para hacer la superficie opaca.
