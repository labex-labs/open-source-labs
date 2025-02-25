# Crear la segunda subtrama

Crearemos la segunda subtrama con el parámetro `rstride` establecido en `0` y el parámetro `cstride` establecido en `10`.

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
