# Add Subplots to the Inner GridSpec

Nous allons maintenant ajouter des sous-graphes au gridspec interne. Nous allons créer trois sous-graphes : `ax1`, `ax2` et `ax3`.

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
