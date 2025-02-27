# Entraîner des classifieurs

- Créer une grille logarithmique des paramètres `gamma` et `C` à l'aide de `np.logspace`.
- Diviser les données en ensembles d'entraînement et de test à l'aide de `StratifiedShuffleSplit`.
- Effectuer une recherche de grille à l'aide de `GridSearchCV` pour trouver les meilleurs paramètres pour le modèle SVM.
- Ajuster un classifieur pour tous les paramètres dans la version 2D.
