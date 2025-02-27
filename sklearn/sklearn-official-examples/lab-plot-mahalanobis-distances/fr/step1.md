# Générer des données

Tout d'abord, nous générons un ensemble de données de 125 échantillons et 2 caractéristiques. Les deux caractéristiques sont distribuées selon une loi normale avec une moyenne de 0. Cependant, la caractéristique 1 a un écart-type égal à 2 et la caractéristique 2 a un écart-type égal à 1. Ensuite, nous remplaçons 25 échantillons par des échantillons aberrants gaussiens où la caractéristique 1 a un écart-type égal à 1 et la caractéristique 2 a un écart-type égal à 7.

```python
import numpy as np

# for consistent results
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# generate Gaussian data of shape (125, 2)
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# add some outliers
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
