# Tracez les données dans le premier sous-graphique

Tracez le cosinus des valeurs de x dans le premier sous-graphique à l'aide de la fonction plot de matplotlib.pyplot. Utilisez le paramètre xunits pour spécifier que l'axe des abscisses doit être en radians.

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
