# Tracer des lignes

Dans cette étape, nous allons tracer un ensemble de lignes à l'aide de la bibliothèque Matplotlib. Tout d'abord, nous créons des données aléatoires à l'aide de NumPy. Ensuite, nous définissons le cycle de couleurs à l'aide de la fonction `cycler` pour spécifier la carte de couleurs. Enfin, nous traçons les données à l'aide de la fonction `plot` et appelons `legend()` pour générer la légende.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixer l'état aléatoire pour la reproductibilité
np.random.seed(19680801)

# Créer des données aléatoires
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# Définir le cycle de couleurs
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# Tracer les données et générer la légende
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```
