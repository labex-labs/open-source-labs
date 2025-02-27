# Bornes théoriques

La première étape consiste à explorer les bornes théoriques du lemme de Johnson-Lindenstrauss. Nous allons tracer le nombre minimum de dimensions nécessaire pour garantir un plongement `eps` pour un nombre croissant d'échantillons `n_samples`. La distorsion introduite par une projection aléatoire `p` est affirmée par le fait que `p` définit un plongement `eps` avec une bonne probabilité comme défini par :

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

Où `u` et `v` sont deux lignes prises au hasard d'un ensemble de données de forme `(n_samples, n_features)` et `p` est une projection par une matrice gaussienne aléatoire `N(0, 1)` de forme `(n_components, n_features)` (ou une matrice d'Achlioptas sparse).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# plage de distorsions admissibles
eps_range = np.linspace(0.1, 0.99, 5)
couleurs = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# plage du nombre d'échantillons (observations) à plonger
n_samples_range = np.logspace(1, 9, 9)

plt.figure()
for eps, couleur in zip(eps_range, couleurs):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples_range, eps=eps)
    plt.loglog(n_samples_range, min_n_components, couleur=couleur)

plt.legend([f"eps = {eps:0.1f}" for eps in eps_range], loc="bas droite")
plt.xlabel("Nombre d'observations pour un plongement eps")
plt.ylabel("Nombre minimum de dimensions")
plt.title("Bornes de Johnson-Lindenstrauss :\nn_samples vs n_components")
plt.show()
```
