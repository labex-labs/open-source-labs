# Ajuster l'alignement des étiquettes d'échelle

Enfin, nous pouvons utiliser les méthodes `set_ha` et `set_va` pour ajuster l'alignement horizontal et vertical des étiquettes d'échelle.

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```
