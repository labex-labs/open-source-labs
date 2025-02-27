# Calcul de l'information mutuelle

Nous allons maintenant calculer le score d'information mutuelle pour chaque caractéristique. L'information mutuelle peut capturer n'importe quel type de dépendance entre les variables. Nous allons normaliser les scores d'information mutuelle en les divisant par le score maximal d'information mutuelle.

```python
mi = mutual_info_regression(X, y)
mi /= np.max(mi)
```
