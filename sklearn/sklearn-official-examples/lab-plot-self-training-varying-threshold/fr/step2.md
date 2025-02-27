# Chargement des données

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

Le jeu de données `breast_cancer` est chargé et mélangé. Nous copions ensuite les vraies étiquettes dans `y_true` et supprimons toutes les étiquettes de `y` sauf celles des 50 premiers échantillons. Cela servira à simuler un scénario d'apprentissage semi-supervisé.
