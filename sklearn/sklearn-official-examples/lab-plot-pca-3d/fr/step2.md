# Création des données

Nous allons générer un ensemble de données aléatoires pour ce laboratoire. L'ensemble de données aura trois variables `x`, `y` et `z`. Nous définirons `x` et `y` comme des variables aléatoires distribuées normalement avec une moyenne de 0 et un écart-type de 0,5. `z` est également distribuée normalement avec une moyenne de 0 et un écart-type de 0,1.

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```
