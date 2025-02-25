# Ajuster l'axe parasite

Nous devons ajuster la position des axes parasites. La fonction `new_fixed_axis()` est utilisée pour créer un nouvel axe y du côté droit du graphique. La fonction `toggle()` est utilisée pour activer toutes les graduations et les étiquettes de l'axe y droit.

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```
