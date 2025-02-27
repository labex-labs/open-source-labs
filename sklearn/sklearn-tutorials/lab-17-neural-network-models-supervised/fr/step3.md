# Créez et entraînez le modèle MLP

```python
# Créez un classifieur MLP avec une couche cachée de 5 neurones
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# Entraînez le modèle à l'aide des données d'entraînement
clf.fit(X, y)
```
