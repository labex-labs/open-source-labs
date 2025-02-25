# Créez une figure et un sous-graphique

Nous devons créer une figure et un sous-graphique pour tracer nos données. Nous allons créer un tracé avec deux sous-graphiques.

```python
fig = plt.figure()

ax = fig.add_subplot(211)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")

ax = fig.add_subplot(223)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")
```
