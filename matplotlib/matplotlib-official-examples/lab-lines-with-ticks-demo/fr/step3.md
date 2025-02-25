# Tracer une ligne courbe avec Ticked Patheffect

Nous allons maintenant tracer une ligne courbe avec l'effet de tracé pointillé.

```python
# Tracer une ligne courbe avec le style de tracé pointillé
ax.plot(x, y, label="Courbe", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```
