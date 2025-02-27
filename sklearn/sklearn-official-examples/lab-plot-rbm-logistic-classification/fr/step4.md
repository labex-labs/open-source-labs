# Evaluation

Dans cette étape, nous évaluons les performances du modèle sur l'ensemble de données de test. Nous utilisons la fonction `classification_report` du module `sklearn.metrics` pour générer le rapport de classification pour le modèle de pipeline et le modèle de régression logistique.

```python
from sklearn import metrics

Y_pred = rbm_features_classifier.predict(X_test)
print(
    "Régression logistique utilisant les caractéristiques RBM :\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)

# Entraînement du classifieur de régression logistique directement sur les pixels
raw_pixel_classifier = clone(logistic)
raw_pixel_classifier.C = 100.0
raw_pixel_classifier.fit(X_train, Y_train)

Y_pred = raw_pixel_classifier.predict(X_test)
print(
    "Régression logistique utilisant les caractéristiques de pixel brute :\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)
```
