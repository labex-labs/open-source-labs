# Préparer les données

Nous allons générer des données synthétiques pour la classification. La fonction à classifier est définie comme suit :

```python
def g(x):
    """La fonction à prédire (la classification consistera ensuite à prédire
    si g(x) <= 0 ou non)"""
    return 5.0 - x[:, 1] - 0.5 * x[:, 0] ** 2.0
```

Ensuite, nous devons créer la conception des expériences et les observations.

```python
# Quelques constantes
lim = 8

# Conception des expériences
X = np.array(
    [
        [-4.61611719, -6.00099547],
        [4.10469096, 5.32782448],
        [0.00000000, -0.50000000],
        [-6.17289014, -4.6984743],
        [1.3109306, -6.93271427],
        [-5.03823144, 3.10584743],
        [-2.87600388, 6.74310541],
        [5.21301203, 4.26386883],
    ]
)

# Observations
y = np.array(g(X) > 0, dtype=int)
```
