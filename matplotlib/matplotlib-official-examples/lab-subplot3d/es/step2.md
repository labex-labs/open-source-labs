# Crear la figura y los subgráficos

Crearemos una figura con dos subgráficos. El primer subgráfico será una representación de superficie tridimensional y el segundo subgráfico será una representación de wireframe tridimensional.

```python
# Create a figure with two subplots
fig = plt.figure(figsize=plt.figaspect(0.5))

# Add the first subplot with 3D projection
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Add the second subplot with 3D projection
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```
