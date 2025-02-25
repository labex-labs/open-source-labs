# Agregar datos a la gráfica

Agregamos datos a la gráfica utilizando el método `plot`. Agregamos tres líneas a la gráfica, cada una con un eje y diferente.

```python
p1, = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
p2, = twin1.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")
p3, = twin2.plot([0, 1, 2], [50, 30, 15], "C2", label="Velocity")
```
