# Générer un ensemble de données synthétiques

Nous générons un ensemble de données synthétiques où `X` et `y` sont liés linéairement. Dix des caractéristiques de `X` seront utilisées pour générer `y`. Les autres caractéristiques ne sont pas utiles pour prédire `y`. De plus, nous générons un ensemble de données où `n_samples == n_features`. Un tel paramétrage est difficile pour un modèle OLS et peut potentiellement entraîner des poids arbitrairement grands. Avoir une a priori sur les poids et une pénalité atténue le problème. Enfin, du bruit gaussien est ajouté.

```python
from sklearn.datasets import make_regression

X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)
```
