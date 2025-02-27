# Combiner les objets d'affichage en un seul graphique

Les objets d'affichage stockent les valeurs calculées qui ont été passées en tant qu'arguments. Cela permet de combiner facilement les visualisations à l'aide de l'API de Matplotlib. Dans l'exemple suivant, nous plaçons les affichages côte à côte dans une ligne.

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

roc_display.plot(ax=ax1)
pr_display.plot(ax=ax2)
plt.show()
```
