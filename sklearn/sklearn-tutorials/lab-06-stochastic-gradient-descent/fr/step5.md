# Entraîner le classifieur

Maintenant, nous pouvons créer et entraîner le classifieur SGD à l'aide de la classe SGDClassifier de scikit-learn. Nous utiliserons la fonction de perte 'hinge', qui est couramment utilisée pour les classifieurs linéaires.

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```
