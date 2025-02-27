# Entraîner et tester le classifieur de Régression Logistique

Nous allons maintenant entraîner un classifieur de Régression Logistique à l'aide de la fonction `LogisticRegression` de scikit-learn et le tester sur l'ensemble de test. Nous allons ensuite afficher le score de précision du classifieur.

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```
