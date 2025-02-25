# Tracez les données dans le second sous-graphique

Tracez le cosinus des valeurs de x dans le second sous-graphique à l'aide de la fonction plot de matplotlib.pyplot. Utilisez le paramètre xunits pour spécifier que l'axe des abscisses doit être en degrés.

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
