# Tracé semi-logarithmique (Semilogy Plot)

Le tracé semi-logarithmique est un tracé avec une échelle logarithmique sur l'axe des ordonnées. Il est utile pour visualiser des données qui ont une large plage de valeurs.

```python
import matplotlib.pyplot as plt
import numpy as np

# Données pour le tracé
t = np.arange(0.01, 20.0, 0.01)

# Création de la figure
fig, ax1 = plt.subplots()

# Tracé des données sur le tracé semi-logarithmique
ax1.semilogy(t, np.exp(-t / 5.0))

# Ajout du titre et de la grille au tracé
ax1.set(title='Tracé semi-logarithmique (Semilogy Plot)')
ax1.grid()

# Affichage du tracé
plt.show()
```
