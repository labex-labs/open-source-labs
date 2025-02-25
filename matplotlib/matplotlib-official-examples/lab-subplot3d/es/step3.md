# Crear la representación de superficie tridimensional

Crearemos una representación de superficie tridimensional para el primer subgráfico. Utilizaremos NumPy para crear los datos del gráfico.

```python
# Create data for the 3D surface plot
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the 3D surface plot
surf = ax1.plot_surface(X, Y, Z, cmap='coolwarm', linewidth=0, antialiased=False)

# Add a color bar to the plot
fig.colorbar(surf, shrink=0.5, aspect=10)

# Set the limits for the z-axis
ax1.set_zlim(-1.01, 1.01)
```
