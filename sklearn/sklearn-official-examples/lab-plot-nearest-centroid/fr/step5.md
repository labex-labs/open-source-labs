# Prédisez et mesurez la précision

Nous prédisons les étiquettes de classe pour les données d'entrée et mesurons la précision du classifieur.

```python
y_pred = clf.predict(X)
print("Précision : ", np.mean(y == y_pred))
```
