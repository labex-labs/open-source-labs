# Entraînez un classifieur à l'aide de la SGD

Maintenant, nous allons entraîner un classifieur à l'aide de la classe SGDClassifier. Nous utiliserons la fonction de perte log_loss et la pénalité l2.

```python
# Entraînez un classifieur à l'aide de la SGD
clf = SGDClassifier(loss="log_loss", penalty="l2", max_iter=100, random_state=42)
clf.fit(X_train, y_train)

# Faites des prédictions sur l'ensemble de test
y_pred = clf.predict(X_test)

# Évaluez la précision du classifieur
accuracy = accuracy_score(y_test, y_pred)

# Affichez la précision
print("Précision du classifieur :", accuracy)
```
