# Создаем трехмерную поверхностную диаграмму

Для первого подграфика мы создадим трехмерную поверхностную диаграмму. Мы будем использовать NumPy для создания данных для диаграммы.

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
