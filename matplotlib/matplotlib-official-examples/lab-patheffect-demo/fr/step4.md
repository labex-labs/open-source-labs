# Ajouter un effet d'ombre à la légende

Nous pouvons ajouter un effet d'ombre à une légende en utilisant l'effet de tracé `withSimplePatchShadow`.

```python
# Créer le graphique et ajouter l'effet d'ombre à la légende
fig, ax = plt.subplots()
p1, = ax.plot([0, 1], [0, 1])
leg = ax.legend([p1], ["Ligne 1"], fancybox=True, loc='upper left')
leg.legendPatch.set_path_effects([patheffects.withSimplePatchShadow()])

plt.show()
```
