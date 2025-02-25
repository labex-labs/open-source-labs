# Crear trama 3D

En este paso, crearemos una trama 3D de una onda sinusoidal.

```python
ax2 = fig.add_subplot(2, 1, 2, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        linewidth=0, antialiased=False)
ax2.set_zlim(-1, 1)
```
