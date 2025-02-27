# Fixez les paramètres

Nous devons fixer les paramètres qui contrôlent la taille des jeux de données, le nombre d'itérations et l'écart-type du bruit.

```python
n_repeat = 50  # Nombre d'itérations pour le calcul des espérances
n_train = 50  # Taille de l'ensemble d'entraînement
n_test = 1000  # Taille de l'ensemble de test
noise = 0.1  # Écart-type du bruit
np.random.seed(0)
```
