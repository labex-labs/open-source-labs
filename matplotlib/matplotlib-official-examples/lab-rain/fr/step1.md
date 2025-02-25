# Créer une nouvelle figure et des axes

La première étape consiste à créer une nouvelle figure et des axes qui la remplissent. Ceci sera le canevas sur lequel la simulation sera dessinée.

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```
