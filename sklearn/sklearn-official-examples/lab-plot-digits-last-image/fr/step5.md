# Évaluation du modèle

Pour évaluer les performances de notre modèle, nous pouvons utiliser la fonction `accuracy_score` de scikit-learn :

```python
from sklearn.metrics import accuracy_score

# Prédit les étiquettes de l'ensemble de test
y_pred = clf.predict(X_test)

# Calcule la précision du modèle
accuracy = accuracy_score(y_test, y_pred)

# Affiche la précision du modèle
print("Précision :", accuracy)
```
