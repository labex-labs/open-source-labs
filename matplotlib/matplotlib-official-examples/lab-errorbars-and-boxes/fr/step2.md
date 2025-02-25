# Préparer les données

Nous allons ensuite préparer les données pour notre diagramme en boîte. Nous allons créer des données fictives pour les valeurs x et y, ainsi que pour les valeurs d'erreur.

```python
# Nombre de points de données
n = 5

# Données fictives
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# Erreurs fictives (au-dessus et en-dessous)
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```
