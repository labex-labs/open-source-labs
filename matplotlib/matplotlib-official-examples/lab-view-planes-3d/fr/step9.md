# Ajoutez une étiquette au sous-graphique central

Nous ajoutons une étiquette au sous-graphique central pour indiquer que ceci est un graphique de plans de vue principales 3D.

```python
label ='mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```
