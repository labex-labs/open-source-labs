# Crear la figura y configurar los ejes

A continuación, crearemos una figura y configuraremos los ejes. Usaremos el método `add_axes()` para crear un nuevo conjunto de ejes dentro de la figura. También estableceremos límites para los ejes x e y y agregaremos líneas de cuadrícula.

```python
# Crear figura y ejes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Establecer límites y líneas de cuadrícula
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```
