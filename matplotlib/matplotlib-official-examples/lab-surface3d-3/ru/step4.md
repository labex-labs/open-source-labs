# Создаем трехмерную поверхностную диаграмму

В этом шаге мы создадим трехмерную поверхностную диаграмму с цветами граней, взятыми из массива, который мы создали. Также настроим ось z.

```python
# Create the surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)

# Customize the z axis
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(6))

# Show the plot
plt.show()
```
