# Füge Achsenbeschriftungen und Stricheneinteilungen hinzu

Füge die x- und y-Achsenbeschriftungen hinzu mit `figtext`. Verberge die oberen und rechten Rahmendenker mit `spines`. Setze benutzerdefinierte Stricheneinteilungen und -beschriftungen mit `set_xticks` und `set_yticks`.

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
