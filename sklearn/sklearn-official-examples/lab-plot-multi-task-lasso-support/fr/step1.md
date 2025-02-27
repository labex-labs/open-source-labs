# Générer des données

Tout d'abord, nous devons générer des données d'échantillonnage que nous pouvons utiliser pour ajuster nos modèles. Nous utiliserons numpy pour générer 100 échantillons, chacun avec 30 caractéristiques et 40 tâches. Nous sélectionnerons également au hasard 5 caractéristiques pertinentes et créerons des coefficients pour elles à l'aide d'ondes sinusoïdales avec une fréquence et une phase aléatoires. Enfin, nous ajouterons du bruit aléatoire aux données.

```python
import numpy as np

rng = np.random.RandomState(42)

# Générer quelques coefficients 2D avec des ondes sinusoïdales avec une fréquence et une phase aléatoires
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```
