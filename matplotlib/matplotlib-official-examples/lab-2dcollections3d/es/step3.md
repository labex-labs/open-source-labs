# Trazar datos bidimensionales en el gráfico tridimensional

El tercer paso es trazar datos bidimensionales en el gráfico tridimensional utilizando `ax.plot` y `ax.scatter`. La función `ax.plot` traza una curva senoidal utilizando los ejes x e y. La función `ax.scatter` traza datos de diagrama de dispersión en los ejes x y z.

```python
# Trazar una curva senoidal utilizando los ejes x e y.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curva en (x, y)')

# Trazar datos de diagrama de dispersión (20 puntos bidimensionales por color) en los ejes x y z.
colors = ('r', 'g', 'b', 'k')

# Fijar el estado aleatorio para la reproducibilidad
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# Al utilizar zdir='y', el valor y de estos puntos se fija en el valor zs 0
# y los puntos (x, y) se trazan en los ejes x y z.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='puntos en (x, z)')
```
