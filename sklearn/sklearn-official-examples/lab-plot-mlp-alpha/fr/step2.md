# Définition des valeurs d'alpha

Nous allons définir différentes valeurs pour le paramètre de régularisation, alpha. Nous utiliserons np.logspace pour générer 5 valeurs espacées logarithmiquement entre 0,1 et 10.

```python
alphas = np.logspace(-1, 1, 5)
```
