# Tracer une ligne droite avec Ticked Patheffect

Nous allons maintenant tracer une ligne diagonale droite avec l'effet de tracé pointillé.

```python
# Tracer une ligne diagonale droite avec le style de tracé pointillé
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Ligne",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])
```
