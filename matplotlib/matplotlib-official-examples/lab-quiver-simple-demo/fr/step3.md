# Création du graphique de flèches

Nous pouvons créer le graphique de flèches à l'aide de la fonction `ax.quiver()`. Nous passons les tableaux `X`, `Y`, `U` et `V` en tant que paramètres.

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```
