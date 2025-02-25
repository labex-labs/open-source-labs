# Générer une ellipse à l'aide d'arcs

Dans cette étape, nous allons générer l'ellipse à l'aide d'arcs.

```python
theta = np.deg2rad(np.arange(0.0, 360.0, 1.0))
x = 0.5 * width * np.cos(theta)
y = 0.5 * height * np.sin(theta)

rtheta = np.radians(angle)
R = np.array([
    [np.cos(rtheta), -np.sin(rtheta)],
    [np.sin(rtheta),  np.cos(rtheta)],
    ])

x, y = np.dot(R, [x, y])
x += xcenter
y += ycenter
```
