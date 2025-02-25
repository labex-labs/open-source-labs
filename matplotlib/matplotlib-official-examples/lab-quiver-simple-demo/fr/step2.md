# Création des données

Nous devons créer les coordonnées `X` et `Y` à l'aide de la fonction `np.meshgrid()`. Ensuite, nous créons les tableaux `U` et `V` qui représentent les champs de vecteurs.

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```
