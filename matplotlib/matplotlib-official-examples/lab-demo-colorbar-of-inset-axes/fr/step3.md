# Créer un axe inséré

Créez un axe inséré à l'aide de la fonction `zoomed_inset_axes`. Réglez le niveau de zoom et l'emplacement de l'axe inséré dans le graphique principal.

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
