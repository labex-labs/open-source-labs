# Agregando datos

Agregaremos los datos al gráfico utilizando la función `plot`. Asignaremos cada línea a una variable para poder hacer referencia a ella más adelante.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Densidad")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperatura")
```
