# Tracer les points de contrôle et les lignes de connexion

Dans cette étape, nous traçons les points de contrôle et les lignes de connexion du tracé à l'aide de la méthode `plot` de l'objet axes.

```python
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
```
