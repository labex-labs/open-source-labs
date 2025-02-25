# Direction/sens des traits de cote

Dans cette étape, nous allons changer le côté des traits de cote.

```python
fig, ax = plt.subplots(figsize=(6, 6))
line_x = line_y = [0, 1]
ax.plot(line_x, line_y, label="Ligne",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

ax.plot(line_x, line_y, label="Côté opposé",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=-135)])

ax.legend()
plt.show()
```

Ce code créera une ligne avec des traits de cote des deux côtés.
