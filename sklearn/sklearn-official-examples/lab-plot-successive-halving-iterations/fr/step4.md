# Création d'un objet de recherche aléatoire par division successive

Créez un objet `HalvingRandomSearchCV` pour explorer l'espace de paramètres. L'objet prend les arguments suivants :

- `estimator` : l'estimateur à optimiser
- `param_distributions` : l'espace de paramètres à explorer
- `factor` : le facteur par lequel le nombre de candidats est réduit à chaque itération
- `random_state` : l'état aléatoire utilisé pour la recherche

Le code pour créer l'objet est le suivant :

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```
