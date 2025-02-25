# Tracé semi-logarithmique horizontal (Semilogx Plot)

Le tracé semi-logarithmique horizontal est un tracé avec une échelle logarithmique sur l'axe des abscisses. Il est utile pour visualiser des données qui ont une large plage de valeurs sur l'axe des abscisses.

```python
import matplotlib.pyplot as plt
import numpy as np

# Données pour le tracé
t = np.arange(0.01, 20.0, 0.01)

# Création de la figure
fig, ax2 = plt.subplots()

# Tracé des données sur le tracé semi-logarithmique horizontal
ax2.semilogx(t, np.sin(2 * np.pi * t))

# Ajout du titre et de la grille au tracé
ax2.set(title='Tracé semi-logarithmique horizontal (Semilogx Plot)')
ax2.grid()

# Affichage du tracé
plt.show()
```
