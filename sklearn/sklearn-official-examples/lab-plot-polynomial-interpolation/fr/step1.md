# Préparer les données

Nous commençons par définir une fonction que nous souhaitons approcher et préparons le tracé de cette fonction.

```python
def f(x):
    """Fonction à approcher par interpolation polynomiale."""
    return x * np.sin(x)

# plage totale que nous voulons tracer
x_plot = np.linspace(-1, 11, 100)

# Pour rendre cela intéressant, nous ne donnons qu'un petit sous-ensemble de points pour l'entraînement.
x_train = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
x_train = np.sort(rng.choice(x_train, size=20, replace=False))
y_train = f(x_train)

# créer des versions de tableaux 2D de ces tableaux pour alimenter les transformateurs
X_train = x_train[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]
```
