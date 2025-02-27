# Chargement du jeu de données et création de poids d'échantillonnage

Nous commençons par charger le jeu de données et créer quelques poids d'échantillonnage. Nous utilisons la fonction `make_regression` de scikit-learn pour générer un jeu de données de régression aléatoire avec 100 000 échantillons. Ensuite, nous générons un vecteur de poids lognormal et le normalisons pour qu'il somme au nombre total d'échantillons.

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalize the sample weights
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```
