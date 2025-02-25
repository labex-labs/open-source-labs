# Désactiver les étiquettes d'échelle

Pour supprimer les étiquettes d'échelle de chacun des insets, nous pouvons utiliser la méthode `tick_params()` et définir `labelleft` et `labelbottom` sur `False`.

```python
# Désactive les étiquettes d'échelle des insets
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```
