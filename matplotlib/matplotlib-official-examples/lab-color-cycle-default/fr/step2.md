# Définissez le cycle de propriétés et récupérez les couleurs

Ensuite, nous devons définir le cycle de propriétés et en extraire les couleurs.

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```
