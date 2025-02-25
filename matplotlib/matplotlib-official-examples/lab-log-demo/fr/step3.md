# Tracé logarithmique double (Loglog Plot)

Le tracé logarithmique double est un tracé avec une échelle logarithmique sur l'axe des abscisses et sur l'axe des ordonnées. Il est utile pour visualiser des données qui ont une large plage de valeurs sur les deux axes.

```python
import matplotlib.pyplot as plt
import numpy as np

# Données pour le tracé
t = np.arange(0.01, 20.0, 0.01)

# Création de la figure
fig, ax3 = plt.subplots()

# Tracé des données sur le tracé logarithmique double
ax3.loglog(t, 20 * np.exp(-t / 10.0))

# Définition de l'échelle de l'axe des abscisses en base 2
ax3.set_xscale('log', base=2)

# Ajout du titre et de la grille au tracé
ax3.set(title='Tracé logarithmique double (Loglog Plot)')
ax3.grid()

# Affichage du tracé
plt.show()
```
