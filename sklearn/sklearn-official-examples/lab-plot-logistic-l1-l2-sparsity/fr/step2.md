# Charger l'ensemble de données

Nous allons charger l'ensemble de données des chiffres à l'aide de `datasets.load_digits(return_X_y=True)`. Nous allons également standardiser les données à l'aide de `StandardScaler().fit_transform(X)`. La variable cible sera binaire, où 0-4 sera classé comme 0 et 5-9 sera classé comme 1.

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```
