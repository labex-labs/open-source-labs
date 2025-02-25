# Configurar la gráfica

Ahora configuraremos la gráfica para nuestra simulación. Crearemos una figura con límites x e y iguales a la longitud máxima del péndulo, estableceremos la relación de aspecto para que sea igual y agregaremos una cuadrícula.

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```
