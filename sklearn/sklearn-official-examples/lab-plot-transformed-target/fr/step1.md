# Importez les bibliothèques nécessaires et chargez des données synthétiques

Nous commençons par importer les bibliothèques nécessaires et charger des données synthétiques. Nous générons un ensemble de données de régression aléatoire synthétique et modifions les cibles en translatant toutes les cibles de manière à ce que toutes les entrées soient non négatives et en appliquant une fonction exponentielle pour obtenir des cibles non linéaires qui ne peuvent pas être ajustées à l'aide d'un modèle linéaire simple. Nous utilisons ensuite une fonction logarithmique (np.log1p) et une fonction exponentielle (np.expm1) pour transformer les cibles avant d'entraîner un modèle de régression linéaire et de l'utiliser pour la prédiction.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Générez des données synthétiques
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modifiez les cibles
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
