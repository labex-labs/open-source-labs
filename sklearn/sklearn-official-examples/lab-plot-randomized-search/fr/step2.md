# Créez un modèle SVM

Nous allons créer un modèle SVM linéaire avec entraînement SGD.

```python
# créez un modèle SVM avec entraînement SGD
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```
