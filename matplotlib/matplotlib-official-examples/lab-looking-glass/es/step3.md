# Creando la figura y los ejes

Crearemos el objeto figura y los ejes utilizando la función `subplots()`. También agregaremos un parche de círculo amarillo al objeto de ejes utilizando la función `patches.Circle()`.

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
