# Générer un ensemble de données

Ensuite, nous allons générer un ensemble de données qui suit une courbe sinusoïdale bruyante.

```python
# Paramètres
n_samples = 100

# Générer un échantillon aléatoire suivant une courbe sinusoïdale
np.random.seed(0)
X = np.zeros((n_samples, 2))
step = 4.0 * np.pi / n_samples

for i in range(X.shape[0]):
    x = i * step - 6.0
    X[i, 0] = x + np.random.normal(0, 0.1)
    X[i, 1] = 3.0 * (np.sin(x) + np.random.normal(0, 0.2))
```
