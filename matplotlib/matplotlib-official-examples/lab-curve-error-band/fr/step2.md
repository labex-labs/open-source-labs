# Définir la courbe

Ensuite, nous définissons la courbe autour de laquelle nous voulons tracer la bande d'erreur. Dans cet exemple, nous utiliserons une courbe paramétrée. Une courbe paramétrée \(x(t), y(t)\) peut être dessinée directement à l'aide de `~.Axes.plot`.

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```
