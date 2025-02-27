# Charger et mélanger les données

Nous commençons par charger l'ensemble de données de chiffres et mélangeons aléatoirement les données.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```
