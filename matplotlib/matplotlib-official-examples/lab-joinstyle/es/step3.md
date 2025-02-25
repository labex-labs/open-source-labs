# Estableciendo JoinStyle

Podemos establecer el `JoinStyle` de la línea usando el método `set_solid_joinstyle()` del objeto `Line2D`. Crearemos un nuevo objeto de línea y estableceremos su estilo de unión en `JoinStyle.bevel`.

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
