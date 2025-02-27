# Générer les données

Dans cette étape, nous générons des données en utilisant la fonction `numpy.random.RandomState` et les paramètres définis dans l'Étape 3.

```python
rng = np.random.RandomState(random_state)
X = np.vstack(
    [
        rng.multivariate_normal(means[j], covars[j], samples[j])
        for j in range(n_components)
    ]
)
y = np.concatenate([np.full(samples[j], j, dtype=int) for j in range(n_components)])
```
