# Bordes adherentes

Algunas funciones de trazado en Matplotlib hacen que los límites del eje sean "adherentes" o inmunes al método `margins()`. Por ejemplo, `imshow()` y `pcolor()` esperan que el usuario desee que los límites estén ajustados alrededor de los píxeles mostrados en la gráfica. Si este comportamiento no es deseado, es necesario establecer `use_sticky_edges` en `False`. En este paso, aprenderemos a evitar los bordes adherentes en Matplotlib.

```python
# crea una cuadrícula
y, x = np.mgrid[:5, 1:6]

# define las coordenadas del polígono
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# crea subgráficos
fig, (ax1, ax2) = plt.subplots(ncols=2)

# utiliza bordes adherentes para ax1 y desactiva los bordes adherentes para ax2
ax2.use_sticky_edges = False

# traza en ambos subgráficos
for ax, status in zip((ax1, ax2), ('Es', 'No es')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # adherente
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # no adherente
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} Adherente')

plt.show()
```
