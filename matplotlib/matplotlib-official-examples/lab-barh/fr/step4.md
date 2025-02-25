# Préparer les données

Les données du graphique sont préparées dans cette étape. Nous allons créer une liste des noms de personnes, de leur performance et du taux d'erreur.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```
