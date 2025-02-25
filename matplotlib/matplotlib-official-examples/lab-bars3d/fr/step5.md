# Personnaliser les axes

Nous allons maintenant personnaliser les axes du tracé 3D. Nous allons définir les étiquettes pour les axes x, y et z en utilisant respectivement les méthodes `set_xlabel()`, `set_ylabel()` et `set_zlabel()`. Nous allons également définir les graduations sur l'axe y en utilisant la méthode `set_yticks()`.

```python
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_yticks(yticks)
```
