# Ajuster un classifieur Bagging

Maintenant, nous allons ajuster un classifieur Bagging sur les données d'entraînement. Le classifieur Bagging est une méthode d'ensemble qui utilise l'échantillonnage bootstrap pour créer plusieurs modèles de base (souvent des arbres de décision) et combine leurs prédictions en utilisant le vote majoritaire.

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```
