# Créer la figure et les sous-graphiques

La deuxième étape consiste à créer la figure et les sous-graphiques qui seront utilisés pour l'animation. Dans cet exemple, nous créons deux sous-graphiques côte à côte avec des rapports d'aspect différents. Le sous-graphique de gauche est un cercle unitaire, et le sous-graphique de droite est un graphique vide qui sera utilisé pour animer une courbe sinusoidale.

```python
fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
```
