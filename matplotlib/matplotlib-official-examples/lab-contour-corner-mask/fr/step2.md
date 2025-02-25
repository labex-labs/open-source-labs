# Création de données pour le tracé

Dans cette étape, nous allons créer des données pour tracer sur un graphe de niveau. Nous utilisons la fonction `np.meshgrid()` pour créer une grille de points, puis calculons les valeurs de `z` à l'aide des fonctions sinus et cosinus.

```python
# Données à tracer.
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```
