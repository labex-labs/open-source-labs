# Charger l'ensemble de données sur le diabète

Ensuite, nous allons charger l'ensemble de données sur le diabète dans notre programme en utilisant la fonction `load_diabetes()` fournie par scikit-learn. Cette fonction renvoie l'ensemble de données sous forme d'un tuple de deux tableaux - l'un contenant les données de caractéristiques et l'autre contenant les données cibles. Nous allons assigner ces tableaux à `X` et `y` respectivement.

```python
# Load the diabetes dataset
X, y = load_diabetes(return_X_y=True)
```
