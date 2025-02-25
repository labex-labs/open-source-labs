# Controlar los puntos de inicio

En este paso, crearemos un gráfico de flujo con puntos de inicio controlados. El parámetro `start_points` toma una matriz bidimensional que representa los puntos de inicio de las líneas de corriente.

```python
seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1, 0, 1, 2, 2]])

strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2,
                      cmap='autumn', start_points=seed_points.T)
plt.colorbar(strm.lines)
plt.title('Controlling Starting Points')
plt.plot(seed_points[0], seed_points[1], 'bo')
plt.xlim(-w, w)
plt.ylim(-w, w)
plt.show()
```
