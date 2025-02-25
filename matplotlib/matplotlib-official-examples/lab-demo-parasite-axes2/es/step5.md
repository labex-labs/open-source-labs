# Establecer límites y etiquetas de los ejes

Estableceremos los límites y etiquetas de los ejes x e y para cada eje utilizando la función `set()`.

```python
host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```
