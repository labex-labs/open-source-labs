# Création de la figure et des axes

Nous allons créer l'objet figure et axes à l'aide de la fonction `subplots()`. Nous ajouterons également un patch de cercle jaune à l'objet axes à l'aide de la fonction `patches.Circle()`.

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
