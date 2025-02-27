# Entraîner et évaluer le classifieur Naïf Bayésien Gaussien

Maintenant, nous allons entraîner le classifieur Naïf Bayésien Gaussien sur l'ensemble d'entraînement et évaluer ses performances sur l'ensemble de test. Nous utiliserons la classe `GaussianNB` du module `sklearn.naive_bayes`.

```python
from sklearn.naive_bayes import GaussianNB

# Crée un classifieur Naïf Bayésien Gaussien
gnb = GaussianNB()

# Entraîne le classifieur
gnb.fit(X_train, y_train)

# Prédit la variable cible pour l'ensemble de test
y_pred = gnb.predict(X_test)

# Calcule la précision du classifieur
accuracy = (y_pred == y_test).sum() / len(y_test)
print("Précision :", accuracy)
```
