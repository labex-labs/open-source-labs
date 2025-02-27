# Prédire et évaluer le modèle

Nous utiliserons le modèle entraîné pour prédire la valeur des chiffres pour les échantillons dans le sous-ensemble de test. Ensuite, nous évaluerons le modèle en utilisant les méthodes `metrics.classification_report()` et `metrics.ConfusionMatrixDisplay.from_predictions()` de `sklearn.metrics`.

```python
predicted = clf.predict(X_test)

print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Matrice de confusion")
print(f"Matrice de confusion:\n{disp.confusion_matrix}")
```
