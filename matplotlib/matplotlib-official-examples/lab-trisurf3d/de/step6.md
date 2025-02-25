# Die 3D-Oberfläche erstellen

Wir werden die 3D-Oberfläche mit der `plot_trisurf`-Funktion erstellen:

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```
