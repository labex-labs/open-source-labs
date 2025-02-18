# Masquage des axes

Nous allons maintenant masquer les axes (spines) entre les deux sous-graphiques en utilisant `ax1.spines.bottom.set_visible` et `ax2.spines.top.set_visible`.

```python
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
```
