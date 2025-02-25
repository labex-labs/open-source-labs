# Créer un diagramme en barres polaires

Nous allons créer un diagramme en barres polaires en utilisant le paramètre `projection='polar'`.

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```
