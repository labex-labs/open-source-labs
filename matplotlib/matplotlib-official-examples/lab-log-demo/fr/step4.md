# Tracé avec barre d'erreur (Errorbars Plot)

Le tracé avec barre d'erreur est un tracé qui montre les barres d'erreur pour chaque point de données. Si un point de données a une valeur négative, il sera tronqué à 0,1.

```python
import matplotlib.pyplot as plt
import numpy as np

# Données pour le tracé
x = 10.0**np.linspace(0.0, 2.0, 20)
y = x**2.0

# Création de la figure
fig, ax4 = plt.subplots()

# Définition de l'échelle logarithmique pour l'axe des abscisses et l'axe des ordonnées
ax4.set_xscale("log", nonpositive='clip')
ax4.set_yscale("log", nonpositive='clip')

# Tracé des données avec les barres d'erreur
ax4.errorbar(x, y, xerr=0.1 * x, yerr=5.0 + 0.75 * y)

# Définition du titre et de la limite de l'axe des ordonnées
ax4.set(title='Tracé avec barre d'erreur (Errorbars Plot)')
ax4.set_ylim(bottom=0.1)

# Affichage du tracé
plt.show()
```
