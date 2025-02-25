# Crear figura y eje

A continuación, crearemos una figura y un eje utilizando el método `subplots()`. Luego graficaremos dos líneas en el eje y agregaremos una leyenda para distinguirlas.

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
