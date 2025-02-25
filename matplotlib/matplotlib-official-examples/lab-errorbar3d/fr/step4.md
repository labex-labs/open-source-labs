# Ajouter des barre d'erreur au tracé

Nous ajoutons des barre d'erreur à notre tracé en utilisant la méthode `errorbar` de l'objet `Axes3D`. Nous définissons les paramètres `zuplims` et `zlolims` sur des tableaux qui spécifient quels points de données ont des limites supérieure et inférieure. Nous définissons le paramètre `errorevery` pour contrôler la fréquence des barre d'erreur.

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```
