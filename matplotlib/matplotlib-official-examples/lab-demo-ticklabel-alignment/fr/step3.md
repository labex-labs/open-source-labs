# Créer une figure et ajouter des sous-graphiques

Ensuite, nous pouvons créer un objet figure et ajouter trois sous-graphiques en utilisant la fonction `setup_axes`.

```python
fig = plt.figure(figsize=(3, 5))
fig.subplots_adjust(left=0.5, hspace=0.7)

ax = setup_axes(fig, 311)
ax.set_ylabel("ha=droite")
ax.set_xlabel("va=ligne de base")

ax = setup_axes(fig, 312)
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
ax.set_ylabel("ha=center")
ax.set_xlabel("va=haut")

ax = setup_axes(fig, 313)
ax.axis["left"].major_ticklabels.set_ha("gauche")
ax.axis["bottom"].major_ticklabels.set_va("bas")
ax.set_ylabel("ha=gauche")
ax.set_xlabel("va=bas")
```
