# Génération du jeu de données

Nous allons générer deux jeux de données synthétiques ayant la même valeur attendue en utilisant une relation linéaire avec une seule caractéristique `x`. Nous allons ajouter du bruit normal hétéroscédastique et du bruit de Pareto asymétrique aux jeux de données.

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# Bruit normal hétéroscédastique
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# Bruit de Pareto asymétrique
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
