# Entraîner le modèle

Nous allons maintenant entraîner le modèle LOF à l'aide des données d'entraînement. Nous définissons le nombre de voisins à 20 et la nouveauté à vrai. Nous définissons également la contamination à 0,1.

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```
