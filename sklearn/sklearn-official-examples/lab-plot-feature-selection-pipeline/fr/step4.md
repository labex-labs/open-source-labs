# Évaluer le pipeline

Nous allons maintenant évaluer le pipeline sur le sous-ensemble de test en utilisant la méthode `predict`. Le pipeline sélectionnera les 3 caractéristiques les plus informatives sur la base de la valeur F de l'ANOVA, et la fonction `LinearSVC` fera des prédictions sur les caractéristiques sélectionnées.

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```
