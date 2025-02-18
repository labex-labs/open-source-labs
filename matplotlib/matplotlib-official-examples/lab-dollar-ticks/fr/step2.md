# Création du graphique

Ensuite, créons un graphique simple avec lequel travailler. Nous allons utiliser NumPy pour générer des données aléatoires à tracer.

```python
import numpy as np

# Générer des données aléatoires
np.random.seed(19680801)
data = 100 * np.random.rand(20)

# Créer le graphique
fig, ax = plt.subplots()
ax.plot(data)
```
