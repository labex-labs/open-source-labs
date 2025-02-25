# Création de la figure et du sous-graphique

Ensuite, nous créons une figure et ajoutons un sous-graphique avec AxesZero. Cela crée une ligne d'axe avec des étiquettes d'axe x et y, mais sans marques d'échelle ni grilles.

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```
