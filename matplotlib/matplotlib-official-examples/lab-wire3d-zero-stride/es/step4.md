# Crear la primera subtrama

Crearemos la primera subtrama con el parámetro `rstride` establecido en `10` y el parámetro `cstride` establecido en `0`.

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
