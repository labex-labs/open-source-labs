# Calcular el atractor de Lorenz

Calculamos el atractor de Lorenz avanzando en el tiempo y estimando el siguiente punto utilizando el punto anterior y la función de Lorenz.

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```
