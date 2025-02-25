# Création des données

Dans cette étape, nous allons créer les données pour notre graphique à barre d'erreur. Nous utiliserons NumPy pour créer un tableau de valeurs de theta et un tableau de valeurs de rayon correspondantes.

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
