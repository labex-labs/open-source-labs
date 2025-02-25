# Representar los datos

Representaremos tres conjuntos de datos en la misma gráfica: Densidad, Temperatura y Velocidad. Utilizaremos la función `plot()` para representar los datos.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
```
