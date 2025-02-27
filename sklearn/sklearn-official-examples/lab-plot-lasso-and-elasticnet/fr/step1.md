# Générer un ensemble de données synthétiques

Tout d'abord, nous générons un ensemble de données où le nombre d'échantillons est inférieur au nombre total de caractéristiques. Cela conduit à un système sous-déterminé, c'est-à-dire que la solution n'est pas unique et que nous ne pouvons pas appliquer une méthode des moindres carrés ordinaires par elle-même. La régularisation introduit un terme de pénalité dans la fonction objectif, ce qui modifie le problème d'optimisation et peut aider à atténuer la nature sous-déterminée du système. Nous allons générer une variable cible `y` qui est une combinaison linéaire de signaux sinusoidaux avec des signes alternés. Seulement les 10 fréquences les plus basses sur les 100 fréquences de `X` sont utilisées pour générer `y`, tandis que les autres caractéristiques ne sont pas informatives. Cela résulte en un espace de caractéristiques creux à haute dimension, où un certain degré de pénalisation L1 est nécessaire.

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # sparsify coef
y = np.dot(X, true_coef)

# introduce random phase using numpy.random.random_sample
# add some gaussian noise using numpy.random.normal
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# split the data into train and test sets using train_test_split from sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
